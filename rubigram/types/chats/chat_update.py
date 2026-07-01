from typing import Any
from dataclasses import dataclass,field

from rubigram.enums import MessageAction, ChatType
from rubigram.types.base import Base
from .chat import Chat
from rubigram.types.updates import UpdatedParameters


@dataclass(repr=False)
class ChatUpdate(Base):
    object_guid: str
    action: MessageAction
    chat: "Chat"
    updated_parameters: "UpdatedParameters"
    timestamp: str
    type: ChatType
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "ChatUpdate":
        data.update(kwargs)
        return cls(
            object_guid=str(data.get("object_guid")),
            action=MessageAction(data.get("action")),
            chat=Chat.read(data.get("chat", {})),
            updated_parameters=UpdatedParameters.read(
                data.get("updated_parameters", [])
            ),
            timestamp=str(data.get("timestamp")),
            type=ChatType[data.get("type")],
            raw=data
        )
