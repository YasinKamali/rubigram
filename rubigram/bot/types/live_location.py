#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base
from rubigram.bot.types import Location
from rubigram.bot.enums import LiveLocationStatus

from dataclasses import dataclass


@dataclass()
class LiveLocation(Base):
    start_time: Optional[str] = None
    live_period: Optional[int] = None
    current_location: Optional["Location"] = None
    user_id: Optional[str] = None
    status: Optional["LiveLocationStatus"] = None
    last_update_time: Optional[str] = None

    def write(self) -> dict[str, Any]:
        current_location = self.current_location.write() if self.current_location else None
        return {
            "start_time": self.start_time,
            "live_period": self.live_period,
            "current_location": current_location,
            "user_id": self.user_id,
            "status": self.status.value,
            "last_update_time": self.last_update_time,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "LiveLocation":
        current_location = data.get("current_location")
        status = data.get("status")
        return cls(
            start_time=data.get("start_time"),
            live_period=data.get("live_period"),
            current_location=Location.read(
                current_location) if current_location else None,
            user_id=data.get("user_id"),
            status=LiveLocationStatus(status) if status else None,
            last_update_time=data.get("last_update_time")
        )