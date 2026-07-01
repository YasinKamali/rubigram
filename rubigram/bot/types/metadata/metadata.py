#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from .metadata_parts import MetadataParts

from dataclasses import dataclass


@dataclass()
class Metadata(Base):
    meta_data_parts: Optional[list["MetadataParts"]] = None

    def write(self) -> dict[str, Any]:
        return {
            "meta_data_parts": [part.write() for part in self.meta_data_parts],
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Metadata":
        meta_data_parts = data.get("meta_data_parts")
        return cls(
            meta_data_parts=[MetadataParts.read(
                part) for part in meta_data_parts] if meta_data_parts else []
        )