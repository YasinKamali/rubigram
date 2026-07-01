#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base

from dataclasses import dataclass


@dataclass()
class ButtonStringPicker(Base):
    items: Optional[list[str]] = None
    default_value: Optional[str] = None
    title: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "items": self.items,
            "default_value": self.default_value,
            "title": self.title
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ButtonStringPicker":
        ...