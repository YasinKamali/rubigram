#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram
from rubigram.bot.enums import ChatKeypadType


class RemoveChatKeypad:
    async def remove_chat_keypad(
        self: "rubigram.Bot",
        chat_id: str,
    ):
        return await self.edit_chat_keypad(chat_id, type=ChatKeypadType.REMOVE)