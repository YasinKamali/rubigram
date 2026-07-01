#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from io import BytesIO
from dataclasses import dataclass
from typing import Optional, Any, cast
from ..base import Base
from rubigram.bot.enums import (
    ParseMode,
    UpdateType,
    ChatKeypadType,
    MessageSenderType,
)
from .. import (
    File,
    Poll,
    Keypad,
    Message,
    AuxData,
    Sticker,
    Location,
    Metadata,
    Propagation,
    LiveLocation,
    ForwardedFrom,
    PaymentStatus,
    ContactMessage,
)
import rubigram


@dataclass()
class Update(Base, Propagation):
    type: "UpdateType"
    chat_id: str
    update_time: Optional[int] = None
    removed_message_id: Optional[str] = None
    new_message: Optional["Message"] = None
    updated_message: Optional["Message"] = None
    updated_payment: Optional["PaymentStatus"] = None
    bot: Optional["rubigram.Bot"] = None

    def write(self) -> dict[str, Any]:
        new_message = self.new_message.write() if self.new_message else None
        updated_message = self.updated_message.write() if self.updated_message else None
        updated_payment = self.updated_payment.write() if self.updated_payment else None
        return {
            "type": self.type.value,
            "chat_id": self.chat_id,
            "update_time": self.update_time,
            "removed_message_id": self.removed_message_id,
            "new_message": new_message,
            "updated_message": updated_message,
            "updated_payment": updated_payment
        }

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Update":
        data.update(kwargs)
        type = data.get('type')
        new_message = data.get("new_message")
        updated_message = data.get("updated_message")
        updated_payment = data.get("updated_payment")
        return cls(
            type=UpdateType(type) if type else None,
            chat_id=data.get("chat_id"),
            update_time=data.get("update_time"),
            removed_message_id=data.get("removed_message_id"),
            new_message=Message.read(new_message) if new_message else None,
            updated_message=Message.read(
                updated_message) if updated_message else None,
            updated_payment=PaymentStatus.read(
                updated_payment) if updated_payment else None,
            bot=cast(rubigram.Bot, data.get("bot"))
        )

    @property
    def text(self) -> Optional[str]:
        if self.new_message:
            return self.new_message.text
        elif self.updated_message:
            return self.updated_message.text
        return None

    @property
    def message_id(self) -> Optional[str]:
        if self.new_message:
            return self.new_message.message_id
        elif self.updated_message:
            return self.updated_message.message_id
        return None

    @property
    def sender_id(self) -> Optional[str]:
        if self.new_message and self.new_message.sender_id:
            return self.new_message.sender_id
        return None

    async def reply(
        self,
        text: str,
        chat_keypad: Optional["Keypad"] = None,
        inline_keypad: Optional["Keypad"] = None,
        chat_keypad_type: Optional["ChatKeypadType"] = None,
        disable_notification: bool = False,
        quote: bool = False,
        metadata: Optional["Metadata"] = None,
        parse_mode: Optional["ParseMode"] = None,
        auto_delete: Optional[int] = None
    ) -> "Message":
        if self.chat_id.startswith("b0") and not quote:
            reply_id = None
        else:
            reply_id = self.message_id

        return await self.bot.send_message(
            chat_id=self.chat_id,
            text=text,
            chat_keypad=chat_keypad,
            inline_keypad=inline_keypad,
            chat_keypad_type=chat_keypad_type,
            metadata=metadata,
            parse_mode=parse_mode,
            disable_notification=disable_notification,
            reply_to_message_id=reply_id,
            auto_delete=auto_delete
        )
