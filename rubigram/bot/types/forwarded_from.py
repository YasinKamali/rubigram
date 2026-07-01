#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base
from rubigram.bot.enums import ForwardedFromType

from dataclasses import dataclass


@dataclass()
class ForwardedFrom(Base):
    type_from: Optional["ForwardedFromType"] = None
    message_id: Optional[str] = None
    from_chat_id: Optional[str] = None
    from_sender_id: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "type_from": self.type_from.value,
            "message_id": self.message_id,
            "from_chat_id": self.from_chat_id,
            "from_sender_id": self.from_sender_id,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ForwardedFrom":
        type_from = data.get("type_from")
        return cls(
            type_from=ForwardedFromType(type_from) if type_from else None,
            message_id=data.get("message_id"),
            from_chat_id=data.get("from_chat_id"),
            from_sender_id=data.get("from_sender_id")
        )