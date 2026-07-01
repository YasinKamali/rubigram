#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import inspect

import rubigram


class Start:
    async def start(
        self: "rubigram.Bot"
    ):
        await self.connection.connect()
        self.load_plugins()
        handler = self.start_handler
        self.me = await self.get_me()

        if handler is None:
            return

        if inspect.iscoroutinefunction(handler):
            await handler(self)
        else:
            handler(self)
