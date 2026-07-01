#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram
from rubigram.bot.types import Keypad


class EditMessageKeypad:
    async def edit_message_keypad(
        self: "rubigram.Bot",
        chat_id: str,
        message_id: str,
        keypad: "Keypad"
    ) -> dict:
        return await self.invoke("editMessageKeypad", {
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_keypad": keypad.write()
        })