#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional

import rubigram
from rubigram.bot.types import Message


class ForwardMessage:
    async def forward_message(
        self: "rubigram.Bot",
        from_chat_id: str,
        message_id: str,
        to_chat_id: str,
        disable_notification: bool = False,
        auto_delete: Optional[int] = None,
    ) -> "Message":
        response = await self.invoke("forwardMessage", {
            "from_chat_id": from_chat_id,
            "message_id": message_id,
            "to_chat_id": to_chat_id,
            "disable_notification": disable_notification
        })
        message = Message.read(response)
        message.bot = self
        message.chat_id = to_chat_id

        if auto_delete := auto_delete or self.auto_delete:
            await self.auto_delete_message(message, auto_delete)

        return message