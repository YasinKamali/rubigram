#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import html
from io import BytesIO
from dataclasses import dataclass
from typing import Optional, Union, Any


from ..base import Base
from rubigram.bot.enums import (
    ParseMode,
    ChatKeypadType,
    MessageSenderType,
)
from .. import (
    File,
    Poll,
    Keypad,
    AuxData,
    Sticker,
    Location,
    Metadata,
    LiveLocation,
    ForwardedFrom,
    ContactMessage
)
import rubigram


@dataclass()
class Message(Base):
    message_id: str
    text: Optional[str] = None
    time: Optional[str] = None
    is_edited: Optional[bool] = None
    sender_type: Optional["MessageSenderType"] = None
    sender_id: Optional[str] = None
    aux_data: Optional["AuxData"] = None
    file: Optional["File"] = None
    reply_to_message_id: Optional[str] = None
    forwarded_from: Optional["ForwardedFrom"] = None
    forwarded_no_link: Optional[str] = None
    location: Optional["Location"] = None
    sticker: Optional["Sticker"] = None
    contact_message: Optional["ContactMessage"] = None
    poll: Optional[Poll] = None
    live_location: Optional["LiveLocation"] = None
    metadata: Optional["Metadata"] = None
    chat_id: Optional[str] = None
    file_id: Optional[str] = None
    bot: Optional["rubigram.Bot"] = None

    def write(self) -> dict[str, Any]:
        aux_data = self.aux_data.write() if self.aux_data else None
        file = self.file.write() if self.file else None
        forwarded_from = self.forwarded_from.write() if self.forwarded_from else None
        location = self.location.write() if self.location else None
        sticker = self.sticker.write() if self.sticker else None
        contact_message = self.contact_message.write() if self.contact_message else None
        poll = self.poll.write() if self.poll else None
        live_location = self.live_location.write() if self.live_location else None
        metadata = self.metadata.write() if self.metadata else None
        return {
            "message_id": self.message_id,
            "text": self.text,
            "time": self.time,
            "is_edited": self.is_edited,
            "sender_type": self.sender_type.value,
            "sender_id": self.sender_id,
            "aux_data": aux_data,
            "file": file,
            "reply_to_message_id": self.reply_to_message_id,
            "forwarded_from": forwarded_from,
            "forwarded_no_link": self.forwarded_no_link,
            "location": location,
            "sticker": sticker,
            "contact_message": contact_message,
            "poll": poll,
            "live_location": live_location,
            "metadata": metadata
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Message":
        sender_type = data.get("sender_type")
        aux_data = data.get("aux_data")
        file = data.get("file")
        forwarded_from = data.get("forwarded_from")
        location = data.get("location")
        sticker = data.get("sticker")
        contact_message = data.get("contact_message")
        poll = data.get("poll")
        live_location = data.get("live_location")
        metadata = data.get("metadata")
        return cls(
            message_id=data.get("message_id"),
            text=data.get("text"),
            time=data.get("time"),
            is_edited=data.get("is_edited"),
            sender_type=MessageSenderType(
                sender_type) if sender_type else None,
            sender_id=data.get("sender_id"),
            reply_to_message_id=data.get("reply_to_message_id"),
            forwarded_no_link=data.get("forwarded_no_link"),
            aux_data=AuxData.read(aux_data) if aux_data else None,
            file=File.read(file) if file else None,
            forwarded_from=ForwardedFrom.read(
                forwarded_from) if forwarded_from else None,
            location=Location.read(location) if location else None,
            sticker=Sticker.read(sticker) if sticker else None,
            contact_message=ContactMessage.read(
                contact_message) if contact_message else None,
            poll=Poll.read(poll) if poll else None,
            live_location=LiveLocation.read(
                live_location) if live_location else None,
            metadata=Metadata.read(metadata) if metadata else None,
        )

    @property
    def mention(self):
        def func(text: Optional[str] = None) -> str:
            if not self.sender_id:
                raise ValueError("Cannot mention without sender_id")
            name = html.escape(text or self.sender_id)
            return f"[{name}]({self.sender_id})"
        return func

    @property
    def effective_file_id(self) -> Optional[str]:
        return self.file.file_id if self.file else self.file_id

    async def reply(
        self,
        text: str,
        chat_keypad: Optional["Keypad"] = None,
        inline_keypad: Optional["Keypad"] = None,
        chat_keypad_type: "ChatKeypadType" = ChatKeypadType.NONE,
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
            self.chat_id,
            text,
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification,
            reply_id,
            metadata,
            parse_mode,
            auto_delete
        )

    async def edit_text(
        self,
        text: str,
        metadata: Optional["Metadata"] = None,
        parse_mode: Optional["ParseMode"] = None
    ) -> "Message":

        return await self.bot.edit_message_text(
            chat_id=self.chat_id,
            message_id=self.message_id,
            text=text,
            metadata=metadata,
            parse_mode=parse_mode
        )

    async def delete(self):

        return await self.bot.delete_messages(
            self.chat_id,
            self.message_id
        )