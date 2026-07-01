#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base
from rubigram.bot.types import File

from dataclasses import dataclass


@dataclass()
class Sticker(Base):
    sticker_id: Optional[str] = None
    file: Optional["File"] = None
    emoji_character: Optional[str] = None

    def write(self) -> dict[str, Any]:
        file = self.file.write() if self.file else None
        return {
            "sticker_id": self.sticker_id,
            "file": file,
            "emoji_character": self.emoji_character
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Sticker":
        file = data.get("file")
        return cls(
            sticker_id=data.get("sticker_id"),
            file=File.read(file) if file else None,
            emoji_character=data.get("emoji_character")
        )