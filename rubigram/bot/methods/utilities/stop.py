#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import inspect

import rubigram


class Stop:
    async def stop(
        self: "rubigram.Bot"
    ):
        await self.connection.disconnect()
        handler = self.stop_handler

        if handler is None:
            return

        if inspect.iscoroutinefunction(handler):
            await handler(self)
        else:
            handler(self)