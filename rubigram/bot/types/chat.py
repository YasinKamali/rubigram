#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base
from rubigram.bot.enums import ChatType

from dataclasses import dataclass


@dataclass()
class Chat(Base):
    chat_id: str
    type: "ChatType"
    user_id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    username: Optional[str] = None

    @property
    def full_name(self) -> str:
        return f"{self.first_name or ''} {self.last_name or ''}"

    def write(self) -> dict[str, Any]:
        return {
            "chat_id": self.chat_id,
            "chat_type": self.type.value,
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "title": self.title,
            "username": self.username
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Chat":
        chat_type = data.get("chat_type")
        return cls(
            chat_id=data.get("chat_id"),
            type=ChatType(chat_type) if chat_type else None,
            user_id=data.get("user_id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            title=data.get("title"),
            username=data.get("username")
        )