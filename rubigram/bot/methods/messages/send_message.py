#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional

import rubigram
from rubigram.utils import remvoe_none_value
from rubigram.bot.enums import ChatKeypadType, ParseMode
from rubigram.bot.types import Keypad, Message, Metadata


class SendMessage:
    async def send_message(
        self: "rubigram.Bot",
        chat_id: str,
        text: str,
        chat_keypad: Optional["Keypad"] = None,
        inline_keypad: Optional["Keypad"] = None,
        chat_keypad_type: Optional["ChatKeypadType"] = ChatKeypadType.NONE,
        metadata: Optional["Metadata"] = None,
        parse_mode: Optional["ParseMode"] = None,
        disable_notification: bool = False,
        reply_to_message_id: Optional[str] = None,
        auto_delete: Optional[int] = None
    ) -> "Message":
        if metadata is None:
            text, metadata = self.parser.parse(text, parse_mode)

        data = remvoe_none_value({
            "chat_id": chat_id,
            "text": text,
            "metadata": metadata,
            "chat_keypad": chat_keypad.write() if chat_keypad else None,
            "inline_keypad": inline_keypad.write() if inline_keypad else None,
            "chat_keypad_type": chat_keypad_type.value if chat_keypad_type else None,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id
        })

        response = await self.invoke("sendMessage", data)
        message = Message.read(response or {})
        message.bot = self
        message.chat_id = chat_id

        if auto_delete := auto_delete or self.auto_delete:
            await self.auto_delete_message(message, auto_delete)

        return message