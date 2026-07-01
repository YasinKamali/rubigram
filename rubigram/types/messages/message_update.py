from typing import Optional, Any
from dataclasses import dataclass, field


from .message import Message
from rubigram.types.base import Base
from rubigram.enums import MessageAction, ChatType


@dataclass(repr=False)
class MessageUpdate(Base):
    message_id: str
    action: MessageAction
    message: Message
    updated_parameters: list
    timestamp: str
    prev_message_id: str
    object_guid: str
    type: ChatType
    state: str
    is_scheduled: bool
    # user_guid: str
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "MessageUpdate":
        data.update(kwargs)
        return cls(
            message_id=str(data.get("message_id")),
            action=MessageAction(data.get("action")),
            message=Message.read(data.get("message", {})),
            updated_parameters=data.get("updated_parameters", []),
            timestamp=str(data.get("timestamp")),
            prev_message_id=str(data.get("prev_message_id")),
            object_guid=str(data.get("object_guid")),
            type=ChatType[data.get("type")],
            state=str(data.get("state")),
            is_scheduled=bool(data.get("updated_parameters")),
            raw=data,
        )