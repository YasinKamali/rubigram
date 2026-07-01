#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base

from dataclasses import dataclass


@dataclass()
class ButtonNumberPicker(Base):
    min_value: Optional[str] = None
    max_value: Optional[str] = None
    default_value: Optional[str] = None
    title: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "min_value": self.min_value,
            "max_value": self.max_value,
            "default_value": self.default_value,
            "title": self.title
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ButtonNumberPicker":
        ...