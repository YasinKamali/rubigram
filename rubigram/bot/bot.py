import os
import sys
import time
import logging

from pathlib import Path
from importlib import import_module
from typing import Optional, Callable
from asyncio import AbstractEventLoop, Semaphore
from concurrent.futures.thread import ThreadPoolExecutor as Executor

from rubigram.parser import Parser
from rubigram import utils, Storage
from rubigram.bot.methods import Methods
from rubigram.connection import Connection
from rubigram.bot.dispatcher import Dispatcher
from rubigram.server import Server
from rubigram.bot.enums import ParseMode
from rubigram.bot.handlers import Handler
from rubigram.bot.web import Webhook
from rubigram.bot.types import Bot as Me


logger = logging.getLogger(__name__)


class Bot(Methods):

    WORKERS = min(32, (os.cpu_count() or 0) + 4)
    PARENT_DIR = Path(sys.argv[0]).parent
    WORKDIR = PARENT_DIR

    def __init__(
        self,
        token: str,
        offset_id: Optional[str] = None,
        auto_delete: Optional[int] = None,
        parse_mode: "ParseMode" = ParseMode.MARKDOWN,

        use_webhook: bool = False,
        webhook_url: Optional[str] = None,
        host: str = "127.0.0.1",
        port: int = 8080,
        set_new_webhook: bool = True,

        delay: int = 1,
        retry: int = 3,
        backoff: int = 1,
        workers: int = WORKERS,
        workdir: ... = WORKDIR,

        plugins: Optional[dict] = None,
        timeout: int = 15,
        connect_timeout: int = 20,
        max_connections: int = 100,
        socket_read_timeout: int = 20,

        proxy: Optional[str] = None,
        semaphore: Optional[Semaphore] = None,
        loop: Optional[AbstractEventLoop] = None
    ):
        self.token = token
        self.offset_id = offset_id or f"{int(time.time()):08x}{'0'*16}"
        self.parse_mode = parse_mode
        self.auto_delete = auto_delete

        self.use_webhook = use_webhook
        self.webhook_url = webhook_url
        self.host = host
        self.port = port

        self.delay = delay
        self.retry = retry
        self.backoff = backoff
        self.workers = workers
        self.plugins = plugins

        self.timeout = timeout
        self.connect_timeout = connect_timeout
        self.max_connections = max_connections
        self.socket_read_timeout = socket_read_timeout

        self.proxy = proxy

        self.semaphore = semaphore or Semaphore(workers)
        self.executor = Executor(workers, thread_name_prefix="Handler")

        if isinstance(loop, AbstractEventLoop):
            self.loop = loop
        else:
            loop = utils.get_event_loop()

        self.me: Optional["Me"] = None

        self.stop_handler: Optional[Callable] = None
        self.start_handler: Optional[Callable] = None

        self.storage = Storage()
        self.parser = Parser(parse_mode)

        self.connection = Connection(
            timeout,
            connect_timeout,
            max_connections,
            socket_read_timeout
        )

        self.server = Server(self.connection, retry, delay, backoff, proxy)
        self.set_new_webhook = set_new_webhook

        self.dispatcher = Dispatcher(self)
        if use_webhook:
            self.webhook = Webhook(self)
        else:
            self.webhook = None

        self.API_URL: str = "https://botapi.rubika.ir/v3/{}/".format(token)

    def __enter__(self):
        return self.start()

    def __exit__(self, *args):
        try:
            return self.stop()
        except ConnectionError:
            pass

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, *args):
        try:
            await self.stop()
        except ConnectionError:
            pass

    def load_plugins(self):
        if self.plugins:
            plugins = self.plugins.copy()

            for option in ["include", "exclude"]:
                if plugins.get(option, []):
                    plugins[option] = [
                        (i.split()[0], i.split()[1:] or None)
                        for i in self.plugins[option]
                    ]
        else:
            return

        if plugins.get("enabled", True):
            root = plugins["root"]
            include = plugins.get("include", [])
            exclude = plugins.get("exclude", [])

            count = 0

            if not include:
                for path in sorted(Path(root.replace(".", "/")).rglob("*.py")):
                    module_path = '.'.join(path.parent.parts + (path.stem,))
                    module = import_module(module_path)

                    for name in vars(module).keys():
                        # noinspection PyBroadException
                        try:
                            for handler, group in getattr(module, name).handlers:
                                if isinstance(handler, Handler) and isinstance(group, int):
                                    self.add_handler(handler, group)

                                    logger.info('[{}] [LOAD] {}("{}") in group {} from "{}"'.format(
                                        self.token, type(handler).__name__, name, group, module_path))

                                    count += 1
                        except Exception:
                            pass
            else:
                for path, handlers in include:
                    module_path = root + "." + path
                    warn_non_existent_functions = True

                    try:
                        module = import_module(module_path)
                    except ImportError:
                        logger.warning(
                            '[%s] [LOAD] Ignoring non-existent module "%s"', self.token, module_path)
                        continue

                    if "__path__" in dir(module):
                        logger.warning(
                            '[%s] [LOAD] Ignoring namespace "%s"', self.token, module_path)
                        continue

                    if handlers is None:
                        handlers = vars(module).keys()
                        warn_non_existent_functions = False

                    for name in handlers:
                        # noinspection PyBroadException
                        try:
                            for handler, group in getattr(module, name).handlers:
                                if isinstance(handler, Handler) and isinstance(group, int):
                                    self.add_handler(handler, group)

                                    logger.info('[{}] [LOAD] {}("{}") in group {} from "{}"'.format(
                                        self.token, type(handler).__name__, name, group, module_path))

                                    count += 1
                        except Exception:
                            if warn_non_existent_functions:
                                logger.warning('[{}] [LOAD] Ignoring non-existent function "{}" from "{}"'.format(
                                    self.token, name, module_path))

            if exclude:
                for path, handlers in exclude:
                    module_path = root + "." + path
                    warn_non_existent_functions = True

                    try:
                        module = import_module(module_path)
                    except ImportError:
                        logger.warning(
                            '[%s] [UNLOAD] Ignoring non-existent module "%s"', self.token, module_path)
                        continue

                    if "__path__" in dir(module):
                        logger.warning(
                            '[%s] [UNLOAD] Ignoring namespace "%s"', self.token, module_path)
                        continue

                    if handlers is None:
                        handlers = vars(module).keys()
                        warn_non_existent_functions = False

                    for name in handlers:
                        # noinspection PyBroadException
                        try:
                            for handler, group in getattr(module, name).handlers:
                                if isinstance(handler, Handler) and isinstance(group, int):
                                    self.remove_handler(handler, group)

                                    logger.info('[{}] [UNLOAD] {}("{}") from group {} in "{}"'.format(
                                        self.token, type(handler).__name__, name, group, module_path))

                                    count -= 1
                        except Exception:
                            if warn_non_existent_functions:
                                logger.warning('[{}] [UNLOAD] Ignoring non-existent function "{}" from "{}"'.format(
                                    self.token, name, module_path))

            if count > 0:
                logger.info('[{}] Successfully loaded {} plugin{} from "{}"'.format(
                    self.token, count, "s" if count > 1 else "", root))
            else:
                logger.warning('[%s] No plugin loaded from "%s"',
                               self.token, root)