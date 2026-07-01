from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field
from rubigram.enums import FileType, ChatType


@dataclass()
class LastMessage(Base):
    message_id: str
    type: "FileType"
    text: str
    author_object_guid: str
    is_mine: bool
    author_type: "ChatType"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "LastMessage":
        data.update(kwargs)
        return cls(
            message_id=str(data.get("message_id")),
            type=FileType(data.get("type")),
            text=str(data.get("text")),
            author_object_guid=str(data.get("author_object_guid")),
            is_mine=bool(data.get("is_mine")),
            author_type=ChatType[data.get("author_type")] if data.get("author_type") else None,
            raw=data,
        )
