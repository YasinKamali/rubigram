#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Any

from .base import Base

from dataclasses import dataclass


@dataclass()
class Location(Base):
    longitude: str
    latitude: str

    def write(self) -> dict[str, Any]:
        return {
            "longitude": self.longitude,
            "latitude": self.latitude,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Location":
        return cls(
            longitude=data.get("longitude"),
            latitude=data.get("latitude")
        )