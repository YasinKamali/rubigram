from dataclasses import dataclass

from rubigram.types.base import Base

from enum import Enum


class AuthorType(Enum):
    BOT = "Bot"
    USER = "User"


class ChatMessageType(Enum):
    NOT_MESSAGE = "NotMessage"
    OTHER = "Other"
    TEXT = "Text"


class MetadataType(Enum):
    PRE = "Pre"
    BOLD = "Bold"
    MONO = "Mono"
    LINK = "Link"
    QUOTE = "Quote"
    ITALIC = "Italic"
    STRIKE = "Strike"
    SPOILER = "Spoiler"
    UNDERLINE = "Underline"
    MENTION_TETX = "MentionText"


@dataclass()
class ChatMessage(Base):
    author_object_guid: str
    author_title: str
    author_type: "AuthorType"
    is_mine: bool
    message_id: int
    metadata: ...
    text: str
    type: "ChatMessageType"


@dataclass()
class MetaData(Base):
    meta_data_parts: list["MetaDataPart"]


@dataclass()
class MetaDataPart(Base):
    from_index: int
    length: int
    link: ...
    mention_text_object_guid: str
    type: "MetadataType"