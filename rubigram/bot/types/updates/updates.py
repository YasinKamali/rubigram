#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from .update import Update
from dataclasses import dataclass


@dataclass()
class Updates(Base):
    updates: Optional[list["Update"]] = None
    next_offset_id: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "updates": [update.write() for update in self.updates],
            "next_offset_id": self.next_offset_id,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Updates":
        updates = data.get("updates")
        return cls(
            updates=[Update.read(update)
                     for update in updates] if updates else [],
            next_offset_id=data.get("next_offset_id")
        )