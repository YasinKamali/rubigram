from dataclasses import dataclass
from typing import Optional, Any
from rubigram.types.base import Base
from .color import Color

@dataclass()
class Warning(Base):
    link: ...
    text: str
    title: str
    title_color: "Color"
    warning_id: str

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Warning":
        data.update(**kwargs)
        return cls(
            link=data.get("link"),
            text=data.get("text"),
            title=data.get("title"),
            title_color=Color.read(
                data["title_color"] if data.get("title_color") else None
            ),
            warning_id=data.get("warning_id")
        )