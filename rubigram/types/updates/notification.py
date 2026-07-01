from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field
from rubigram.types import MessageData
from rubigram.enums import NotificationType


@dataclass(repr=False)
class Notification(Base):
    notification_id: str
    type: NotificationType
    title: str
    text: str
    message_data: "MessageData"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Notification":
        data.update(kwargs)
        return cls(
            notification_id=str(data.get("notification_id")),
            type=NotificationType(data.get("type")),
            title=str(data.get("title")),
            text=str(data.get("text")),
            message_data=MessageData.read(data.get("message_data", {})),
            raw=data,
        )
