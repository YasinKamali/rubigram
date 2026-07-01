#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base

from dataclasses import dataclass


@dataclass()
class AuxData(Base):
    start_id: Optional[str] = None
    button_id: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "start_id": self.start_id,
            "button_id": self.button_id,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "AuxData":
        return cls(
            start_id=data.get("start_id"),
            button_id=data.get("button_id")
        )