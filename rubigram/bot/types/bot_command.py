#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Any

from .base import Base

from dataclasses import dataclass


@dataclass()
class BotCommand(Base):
    command: str
    description: str

    def write(self) -> dict[str, Any]:
        return {
            "command": self.command,
            "description": self.description,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "BotCommand":
        return cls(
            command=data.get("command"),
            description=data.get("description")
        )