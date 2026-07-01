#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base

from dataclasses import dataclass


@dataclass()
class ContactMessage(Base):
    phone_number: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "phone_number": self.phone_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ContactMessage":
        return cls(
            phone_number=data.get("phone_number"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name")
        )