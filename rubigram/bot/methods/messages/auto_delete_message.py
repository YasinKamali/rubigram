#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import logging
import asyncio
from typing import Union

import rubigram
from rubigram.bot.types import Message


logger = logging.getLogger(__name__)


class AutoDeleteMessage:
    async def _create_delete_message_task(
        self: "rubigram.Bot",
        chat_id: str,
        message_id: Union[str, list[str]],
        sleep: Union[int, float]
    ):
        await asyncio.sleep(sleep)
        try:
            await self.delete_messages(chat_id, message_id)
        except asyncio.TimeoutError:
            logger.error("Timeout error to deleted message")
        except Exception as error:
            logger.error("An unexpected error to deleted message: %s", error)

    async def auto_delete_message(
        self: "rubigram.Bot",
        message: "Message",
        sleep: Union[int, float]
    ):
        if sleep > 0:
            logger.info("Run a task to delete the message, sleep: %s", sleep)
            asyncio.create_task(self._create_delete_message_task(
                message.chat_id, message.message_id, sleep
            ))