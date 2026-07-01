from typing import Optional, Any
from dataclasses import dataclass, field

import rubigram
from rubigram.types import Base
from rubigram.enums import MessageType, ChatType

from .file_inline import FileInline
from .location import Location
from .contact_message import ContactMessage
from .forwarded_from import ForwardedFrom
from .sticker import Sticker
from .rubino_post import RubinoPost
from .live_data import LiveData


@dataclass(repr=False)
class Message(Base):
    message_id: str
    text: str
    file_inline: Optional["FileInline"]
    location: Optional["Location"]
    contact_message: Optional["ContactMessage"]
    time: str
    is_edited: bool
    forwarded_from: Optional["ForwardedFrom"]
    sticker: Optional["Sticker"]
    type: MessageType
    author_type: ChatType
    author_object_guid: str
    live_data = Optional["LiveData"]
    rubino_post_data = Optional["RubinoPost"]
    allow_transcription: bool
    client: "rubigram.Client"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Message":
        data.update(kwargs)
        return cls(
            message_id=str(data.get("message_id")),
            text=str(data.get("text")),
            file_inline=(
                FileInline.read(data.get("file_inline", {}))
                if data.get("file_inline")
                else None
            ),
            location=(
                Location.read(data.get("location", {}))
                if data.get("location")
                else None
            ),
            contact_message=(
                ContactMessage.read(data.get("contact_message", {}))
                if data.get("contact_message")
                else None
            ),
            time=str(data.get("time")),
            is_edited=bool(data.get("is_edited")),
            forwarded_from=(
                ForwardedFrom.read(data.get("forwarded_from", {}))
                if data.get("forwarded_from")
                else None
            ),
            sticker=(
                Sticker.read(data.get("sticker", {})) if data.get(
                    "sticker") else None
            ),
            type=MessageType(data.get("type")),
            author_type=ChatType[data.get("author_type")] if data.get("author_type") else None,
            author_object_guid=str(data.get("author_object_guid")),
            allow_transcription=bool(data.get("allow_transcription")),
            client=data.get("client"),
            raw=data,
        )