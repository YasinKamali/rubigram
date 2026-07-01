#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from rubigram.bot.enums import MetadataType

from dataclasses import dataclass


@dataclass()
class MetadataParts(Base):
    from_index: int
    length: int
    type: Optional["MetadataType"] = None
    link_url: Optional[str] = None
    mention_text_user_id: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "from_index": self.from_index,
            "length": self.length,
            "type": self.type.value,
            "link_url": self.link_url,
            "mention_text_user_id": self.mention_text_user_id
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "MetadataParts":
        type = data.get("type")
        return cls(
            from_index=data.get("from_index"),
            type=MetadataType(type) if type else None,
            link_url=data.get("link_url"),
            mention_text_user_id=data.get("mention_text_user_id")
        )