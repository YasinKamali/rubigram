#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Any

from ..base import Base
from .keypad_row import KeypadRow

from dataclasses import dataclass


@dataclass()
class Keypad(Base):
    rows: list["KeypadRow"]
    resize_keyboard: bool = True
    on_time_keyboard: bool = False

    def write(self) -> dict[str, Any]:
        return {
            "rows": [row.write() for row in self.rows],
            "resize_keyboard": self.resize_keyboard,
            "on_time_keyboard": self.on_time_keyboard,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "KeypadRow":
        return cls(
            buttons=[KeypadRow.read(row) for row in data.get("rows")],
            resize_keyboard=data.get("resize_keyboard"),
            on_time_keyboard=data.get("on_time_keyboard")
        )