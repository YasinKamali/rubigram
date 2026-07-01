#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import inspect
from typing import Callable, Optional, Union

import rubigram
from rubigram.bot.filters import Filter
from rubigram.bot.types import Update, InlineMessage


class Handler:
    def __init__(
        self,
        callback: Callable,
        filters: Optional["Filter"] = None
    ):
        self.callback = callback
        self.filters = filters

    async def execute(
        self,
        bot: "rubigram.Bot",
        update: Union["Update", "InlineMessage"]
    ):

        if self.filters is None:
            return True, await self.callback(bot, update)

        if callable(self.filters):
            if inspect.iscoroutinefunction(self.filters.__call__):
                result = await self.filters(bot, update)
            else:
                result = self.filters(bot, update)

            if result:
                return True, await self.callback(bot, update)

            return False, None