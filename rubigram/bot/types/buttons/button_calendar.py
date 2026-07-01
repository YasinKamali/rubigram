#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from rubigram.bot.enums import ButtonCalendarType

from dataclasses import dataclass


@dataclass()
class ButtonCalendar(Base):
    default_value: Optional[str] = None
    type: Optional["ButtonCalendarType"] = None
    min_year: Optional[str] = None
    max_year: Optional[str] = None
    title: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "default_value": self.default_value,
            "type": self.type.value,
            "min_year": self.min_year,
            "max_year": self.max_year,
            "title": self.title
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ButtonCalendar":
        ...