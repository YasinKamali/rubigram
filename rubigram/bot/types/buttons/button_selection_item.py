#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from rubigram.bot.enums import ButtonSelectionType

from dataclasses import dataclass


@dataclass()
class ButtonSelectionItem(Base):
    text: Optional[str] = None
    image_url: Optional[str] = None
    type: Optional["ButtonSelectionType"] = None

    def write(self) -> dict[str, Any]:
        return {
            "text": self.text,
            "image_url": self.image_url,
            "type": self.type.value,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ButtonSelectionItem":
        ...