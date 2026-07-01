from dataclasses import dataclass
from typing import Optional, Any
from rubigram.types.base import Base


@dataclass()
class Color(Base):
    alpha: int
    blue: int
    green: int
    red: int

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Color":
        data.update(**kwargs)
        return cls(
            alpha=data.get("alpha"),
            blue=data.get("blue"),
            green=data.get("green"),
            red=data.get("red")
        )