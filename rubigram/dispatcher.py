#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import logging
import asyncio
from collections import defaultdict
from typing import DefaultDict, Union

import rubigram
from rubigram.types import Update
from rubigram.handlers import Handler
from rubigram import StopPropagation, ContinuePropagation


logger = logging.getLogger(__name__)


class Dispatcher:
    def __init__(self, bot: "rubigram.Client"):
        self.bot = bot
        self.handlers: dict[int, list["Handler"]] = {}

    def start(self):
        ...

    def stop(self):
        ...

    def add_handler(
        self,
        handler: "Handler",
        group: int = 0
    ):
        self.handlers.setdefault(group, [])
        self.handlers[group].append(handler)

    def remove_handler(
        self,
        handler: "Handler",
        group: int = 0
    ):
        if group in self.handlers and handler in self.handlers[group]:
            self.handlers[group].remove(handler)

    async def dispatch(
        self,
        raw_update: dict
    ):
        update = Update.read(raw_update or {})
        for group in sorted(self.handlers):
            for handler in self.handlers.get(group):

                try:
                    status = await handler.execute(update.client, update)
                    if status:
                        continue
                except ContinuePropagation:
                    continue
                except StopPropagation:
                    raise