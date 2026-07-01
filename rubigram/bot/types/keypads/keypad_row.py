#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Any

from ..base import Base
from ..buttons import Button

from dataclasses import dataclass


@dataclass()
class KeypadRow(Base):
    buttons: list["Button"]

    def write(self) -> dict[str, Any]:
        return {
            "buttons": [button.write() for button in self.buttons],
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "KeypadRow":
        return cls(
            buttons=[Button.read(button) for button in data.get("buttons")]
        )