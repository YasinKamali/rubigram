#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional

import rubigram
from rubigram.utils import remvoe_none_value
from rubigram.bot.enums import ChatKeypadType
from rubigram.bot.types import Keypad, Message


class SendContact:
    async def send_contact(
        self: "rubigram.Bot",
        chat_id: str,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        chat_keypad: Optional["Keypad"] = None,
        inline_keypad: Optional["Keypad"] = None,
        chat_keypad_type: Optional["ChatKeypadType"] = ChatKeypadType.NONE,
        disable_notification: bool = False,
        reply_to_message_id: Optional[str] = None,
        auto_delete: Optional[int] = None
    ) -> "Message":
        data = remvoe_none_value({
            "chat_id": chat_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "chat_keypad": chat_keypad.write() if chat_keypad else None,
            "inline_keypad": inline_keypad.write() if inline_keypad else None,
            "chat_keypad_type": chat_keypad_type.value,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id
        })
        response = await self.invoke("sendContact", data)
        message = Message.read(response)
        message.bot = self
        message.chat_id = chat_id

        if auto_delete := auto_delete or self.auto_delete:
            await self.auto_delete_message(message, auto_delete)

        return message