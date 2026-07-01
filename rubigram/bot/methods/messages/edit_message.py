#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional

import rubigram
from rubigram.bot.types import Keypad
from rubigram.bot.enums import ParseMode


class EditMessage:
    async def edit_message(
        self: "rubigram.Bot",
        chat_id: str,
        message_id: Optional[str] = None,
        text: Optional[str] = None,
        chat_keypad: Optional["Keypad"] = None,
        inline_keypad: Optional["Keypad"] = None,
        parse_mode: Optional["ParseMode"] = None
    ) -> dict:
        if text:
            return await self.edit_message_text(
                chat_id, message_id, text, parse_mode
            )

        if chat_keypad:
            return await self.edit_chat_keypad(chat_id, chat_keypad)

        if inline_keypad:
            return await self.edit_message_keypad(chat_id, message_id, inline_keypad)