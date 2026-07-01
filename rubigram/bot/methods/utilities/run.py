#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import time
import logging
import asyncio

import rubigram
from rubigram.bot import types


logger = logging.getLogger(__name__)


def is_update_recent(update_time: int, max_delay: float = 0.1) -> bool:
    now = int(time.time())
    return update_time + max_delay >= now


class Run:
    async def _run(
        self: "rubigram.Bot",
        get_updates_limit: int = 1,
        idle_sleep: float = 0.1
    ):
        logger.info("Start bot, offset_id: %s", self.offset_id)
        await self.start()

        # semaphore = asyncio.Semaphore(self.workers)

        async def handle_update(update: types.Update):
            async with self.semaphore:
                try:
                    update.bot = self
                    await self.dispatcher.dispatch(update)
                except Exception as e:
                    logger.error("Handler error: %s", e)

        tasks = set()

        try:
            while True:
                try:
                    updates = await self.get_updates(get_updates_limit, self.offset_id)
                    if not updates.updates:
                        await asyncio.sleep(idle_sleep)
                        continue

                    for update in updates.updates:
                        if is_update_recent(update.update_time):
                            logger.info(
                                "Receive a new update, type: %s", update.type
                            )

                            task = asyncio.create_task(handle_update(update))
                            tasks.add(task)

                            task.add_done_callback(tasks.discard)

                    self.offset_id = updates.next_offset_id

                except (KeyboardInterrupt, asyncio.CancelledError):
                    logger.info(
                        "Stop bot by user, offset_id: %s", self.offset_id
                    )
                    break

                except Exception as e:
                    logger.error(e)
                    continue

        finally:
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)

            await self.stop()
            logger.info("Stop bot, offset_id: %s", self.offset_id)

    def run(
        self: "rubigram.Bot",
        get_updates_limit: int = 1,
        idle_sleep: float = 0.5
    ):
        if self.use_webhook:
            asyncio.run(self.webhook._run())
        else:
            asyncio.run(self._run(get_updates_limit, idle_sleep))