from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field


@dataclass()
class MessageData(Base):
    object_guid: str
    object_type: str
    message_id: int
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "MessageData":
        return cls(
            object_guid=str(data.get("object_guid")),
            object_type=str(data.get("object_type")),
            message_id=int(data.get("message_id", 0)),
            raw=data,
        )
