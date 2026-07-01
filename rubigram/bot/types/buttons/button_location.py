#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from ..location import Location
from rubigram.bot.enums import ButtonLocationType

from dataclasses import dataclass


@dataclass()
class ButtonLocation(Base):
    default_pointer_location: Optional["Location"] = None
    default_map_location: Optional["Location"] = None
    type: Optional["ButtonLocationType"] = None
    title: Optional[str] = None
    location_image_url: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "default_pointer_location": ...,
            "default_map_location": ...,
            "type": self.type.value,
            "title": self.title,
            "location_image_url": self.location_image_url
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ButtonLocation":
        ...