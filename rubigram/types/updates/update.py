from typing import Optional, Any, cast
from dataclasses import dataclass, field

import rubigram
from rubigram.types import Base, Chat, Message
# from . import Notification

from rubigram.enums import ParseMode, MessageAction


@dataclass(repr=False)
class Update(Base):
    object_guid: str
    action: MessageAction
    message: Message
    chat: Chat
    # notification: Notification
    # update_parametrs: UpdatedParameters
    client: "rubigram.Client" = field(repr=False)
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Update":
        data.update(kwargs)

        chat_update: dict = data.get("chat_updates", [{}])[0]
        message_update: dict = data.get("message_updates", [{}])[0]

        chat = chat_update.get("chat", {})
        message = message_update.get("message", {})

        notification = data.get("show_notifications", [{}])[0]
        parameters = chat_update.get("update_parameters", [])

        return cls(
            object_guid=chat_update.get("object_guid"),
            action=MessageAction(message_update.get("action")),
            chat=Chat.read(chat) if chat else None,
            message=Message.read(message) if message else None,
            # notification=Notification.read(notification),
            # update_parameters=UpdatedParameters.read(parameters),
            client=cast(rubigram.Client, data.get("client")),
            raw=data
        )

    async def reply_text(
        self,
        text: str,
        quote: bool = True,
        metadata: ... = None,
        parse_mode: Optional["ParseMode"] = None,
        auto_delete: Optional[int] = None,
    ):
        message = self.message
        if not quote:
            reply_id = None
        else:
            reply_id = message.message_id
        return await self.client.send_message(
            guid=message.author_object_guid,
            text=text,
            reply_to_message_id=reply_id,
            metadata=metadata,
            parse_mode=parse_mode,
            auto_delete=auto_delete,
        )