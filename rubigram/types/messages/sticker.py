from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field
from .sticker_file import StickerFile


@dataclass()
class Sticker(Base):
    emoji_character: str
    w_h_ratio: str
    sticker_id: str
    file: "StickerFile"
    sticker_set_id: str
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Sticker":
        data.update(kwargs)
        return cls(
            emoji_character=str(data.get("emoji_character")),
            w_h_ratio=str(data.get("w_h_ratio")),
            sticker_id=str(data.get("sticker_id")),
            file=StickerFile.read(data.get("file", {})),
            sticker_set_id=str(data.get("sticker_set_id")),
            raw=data,
        )
