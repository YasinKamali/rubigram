from dataclasses import dataclass
from typing import Optional, Any
from rubigram.types.base import Base
from .file_inline import FileInline


@dataclass()
class Badge(Base):
    icon: Optional["FileInline"]
    raw :dict

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Badge":
        data.update(**kwargs)
        return cls(
            icon=FileInline.read(data["icon"]) if data.get("icon") else None,
            raw = data
        )
