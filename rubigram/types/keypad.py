from dataclasses import dataclass

from .base import Base
from .keypad_row import KeypadRow


@dataclass()
class Keypad(Base):
    one_time_keyboard: bool
    resize_keyboard: bool
    rows: list["KeypadRow"]
    state_id: str

    @classmethod
    def read(cls, data: dict):
        return cls(
            one_time_keyboard=bool(data.get("one_time_keyboard")),
            resize_keyboard=bool(data.get("resize_keyboard")),
            rows=[KeypadRow.read(row) for row in data.get("rows", [])],
            state_id=str(data.get("state_id"))
        )
