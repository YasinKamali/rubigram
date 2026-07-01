import logging
import asyncio
import inspect

import rubigram


logger = logging.getLogger(__name__)


class Start:
    async def start(
        self: "rubigram.Client"
    ):
        await self.connect()

        self.me = await self.get_me()
        self.guid = self.me.user_guid

        if self.start_handler:
            await self.start_handler.execute(self, None)
            # if inspect.iscoroutinefunction(self.start_handler.callback):
            #     print(True)
            #     await self.start_handler.execute(self)
            # else:
            #     # await asyncio.to_thread(self.start_handler.execute, self)
            #     await self.loop.run_in_executor(
            #         self.executor,
            #         self.start_handler.execute,
            #         self
            #     )