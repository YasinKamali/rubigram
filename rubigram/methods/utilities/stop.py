import logging
import asyncio
import inspect

import rubigram


logger = logging.getLogger(__name__)


class Stop:
    async def stop(
        self: "rubigram.Client"
    ):
        await self.disconnect()

        if self.stop_handler:
            await self.stop_handler.execute(self, None)
            # if inspect.iscoroutinefunction(self.stop_handler.callback):
            #     await self.stop_handler.execute(self)
            # else:
            #     # await asyncio.to_thread(self.stop_handler.execute, self)
            #     await self.loop.run_in_executor(
            #         self.executor,
            #         self.stop_handler.execute,
            #         self
            #     )