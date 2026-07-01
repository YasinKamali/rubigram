from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field
from rubigram.enums import ChatType


@dataclass()
class ForwardedFrom(Base):
    type_from: "ChatType"
    message_id: str
    object_guid: str
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "ForwardedFrom":
        data.update(kwargs)
        return cls(
            type_from=ChatType[data.get("type_from")],
            message_id=str(data.get("message_id")),
            object_guid=str(data.get("object_guid")),
            raw=data,
        )
