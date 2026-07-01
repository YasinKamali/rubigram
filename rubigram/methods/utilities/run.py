import signal
import logging
import asyncio

from typing import Awaitable, Any

import rubigram


logger = logging.getLogger(__name__)


class Run:
    def run(
        self: "rubigram.Client"
    ):

        async def main_runner():
            await self.start()

            print("Client Started...")
            try:
                if self.dispatcher and self.dispatcher.handlers:
                    while True:
                        await self.get_updates()
                    # await self.get__updates()

            except asyncio.CancelledError:
                print("Shutdown complete.")
            
            except Exception as error:
                print(error)

            finally:
                await self.stop()

        try:
            asyncio.run(main_runner())
        except KeyboardInterrupt:
            print("Close program.")