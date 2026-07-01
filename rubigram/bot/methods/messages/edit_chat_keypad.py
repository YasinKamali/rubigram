#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram

from typing import Optional

import rubigram
from rubigram.bot.types import Keypad
from rubigram.bot.enums import ChatKeypadType


class EditChatKeypad:
    async def edit_chat_keypad(
        self: "rubigram.Bot",
        chat_id: str,
        keypad: Optional["Keypad"],
        type: "ChatKeypadType" = ChatKeypadType.NEW
    ) -> dict:
        data = {"chat_id": chat_id, "chat_keypad_type": type.value}
        if keypad:
            data["chat_keypad"] = keypad.write()

        return await self.invoke("editChatKeypad", data)