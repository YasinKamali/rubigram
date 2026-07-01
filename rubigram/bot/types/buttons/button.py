#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from rubigram.bot.enums import ButtonType
from . import (
    ButtonSelection,
    ButtonCalendar,
    ButtonNumberPicker,
    ButtonStringPicker,
    ButtonLocation,
    ButtonTextbox
)

from dataclasses import dataclass


@dataclass()
class Button(Base):
    id: str
    button_text: str
    type: "ButtonType" = ButtonType.SIMPLE
    button_selection: Optional["ButtonSelection"] = None
    button_calendar: Optional["ButtonCalendar"] = None
    button_number_picker: Optional["ButtonNumberPicker"] = None
    button_string_picker: Optional["ButtonStringPicker"] = None
    button_location: Optional["ButtonLocation"] = None
    button_textbox: Optional["ButtonTextbox"] = None

    def write(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "button_text": self.button_text,
            "type": self.type.value,
            "button_selection": ...,
            "button_calendar": ...,
            "button_number_picker": ...,
            "button_string_picker": ...,
            "button_location": ...,
            "button_textbox": ...,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ButtonCalendar":
        ...