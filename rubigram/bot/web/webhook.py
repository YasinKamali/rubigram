import logging
import asyncio

from aiohttp.web import (
    Request,
    TCPSite,
    AppRunner,
    Application,
    RouteTableDef,
    json_response
)

import rubigram
from rubigram.bot.types import Update, InlineMessage
from rubigram.bot.enums import UpdateEndpointType


logger = logging.getLogger(__name__)


class Webhook:
    def __init__(self, bot: "rubigram.Bot"):
        self.bot = bot
        self.app = Application()
        self.routes = RouteTableDef()
        self.runner = AppRunner(self.app)

        self.host = self.bot.host
        self.port = self.bot.port
        self.url = self.bot.webhook_url

        self.site = None

    async def process_update(self, data: dict):
        if "update" in data:
            update = Update.read(data["update"])
        else:
            update = InlineMessage.read(data["inline_message"])

        await self.bot.dispatcher.dispatch(update)

    def receive_data(self):
        async def wrapper(request: Request):
            try:
                data = await request.json()
                logger.debug("Receive data: %s", data)
                await self.process_update(data)
                return json_response({"status": "OK"})
            except Exception as error:
                logger.error("Error to receive data: %s", error)
                return json_response({"status": "Error", "error": str(error)})

        return wrapper

    async def setup(self):
        if self.bot.set_new_webhook:
            for i in UpdateEndpointType:
                type = i.value
                response = await self.bot.update_bot_endpoints(f"{self.url}/{type}", i)
                logger.info(
                    "Set webhook for %s: %s", type, response.get("status")
                )

                handler = self.receive_data()
                self.routes.post(f"/{type}")(handler)

            self.app.add_routes(self.routes)

    async def start(self):
        await self.bot.start()
        await self.setup()
        await self.runner.setup()
        self.site = TCPSite(self.runner, self.host, self.port)
        await self.site.start()

    async def stop(self):
        await self.bot.stop()
        await self.runner.cleanup()

    async def _run(self):
        await self.start()
        logger.info("Start webhook, url=%s", self.url)
        try:
            await asyncio.Event().wait()
        except (asyncio.CancelledError, KeyboardInterrupt):
            pass
        finally:
            await self.stop()
            logger.info("Shutdown webhook, url=%s", self.url)