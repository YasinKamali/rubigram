from typing import Any, List, Optional
from dataclasses import dataclass, field

from rubigram.enums import ChatStatus
from rubigram.types import Base
from .chat import Chat


@dataclass()
class GetChats(Base):
    chats:List[Chat]
    has_continue:bool
    next_start_id:Optional[str]
    state:str
    timestamp:int
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "GetChats":
        data.update(kwargs)
        return cls(
            chats = [Chat.read(chat) for chat in data.get("chats",[])],
            has_continue = bool(data.get("has_continue")),
            next_start_id = data.get("next_start_id"),
            state = str(data.get("state")),
            timestamp = int(data.get("timestamp",0)),
            raw = data
        )
