#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base
from rubigram.bot.types import File
from dataclasses import dataclass


@dataclass()
class Bot(Base):
    bot_id: str = None
    bot_title: Optional[str] = None
    avatar: Optional["File"] = None
    description: Optional[str] = None
    username: str = None
    start_message: Optional[str] = None
    share_url: str = None

    def write(self) -> dict[str, Any]:
        avatar = self.avatar.write() if self.avatar else None
        return {
            "bot_id": self.bot_id,
            "bot_title": self.bot_title,
            "avatar": avatar,
            "description": self.description,
            "username": self.username,
            "start_message": self.start_message,
            "share_url": self.share_url
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Bot":
        avatar = data.get("avatar")
        return cls(
            bot_id=data.get("bot_id"),
            bot_title=data.get("bot_title"),
            avatar=File.read(avatar) if avatar else None,
            description=data.get("description"),
            username=data.get("username"),
            start_message=data.get("start_message"),
            share_url=data.get("share_url")
        )
