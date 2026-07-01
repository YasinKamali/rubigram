#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from rubigram.bot.enums import ButtonTextboxTypeLine, ButtonTextboxTypeKeypad

from dataclasses import dataclass


@dataclass()
class ButtonTextbox(Base):
    type_line: Optional["ButtonTextboxTypeLine"] = None
    type_keypad: Optional["ButtonTextboxTypeKeypad"] = None
    place_holder: Optional[str] = None
    title: Optional[str] = None
    default_value: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "type_line": self.type_line.value,
            "type_keypad": self.type_keypad.value,
            "place_holder": self.place_holder,
            "title": self.title,
            "default_value": self.default_value
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ButtonTextbox":
        ...