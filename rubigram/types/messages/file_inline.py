from ..base import Base
from typing import Optional, Any
from dataclasses import dataclass, field
from rubigram.enums import FileType


@dataclass()
class FileInline(Base):
    file_id: int
    mime: str
    dc_id: int
    access_hash_rec: str
    file_name: str
    thumb_inline: str
    width: int
    height: int
    time: int
    size: int
    type: Optional[FileType]
    music_performer: Optional[str]
    is_round: bool
    is_spoil: bool
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "FileInline":
        data.update(kwargs)
        return cls(
            file_id=int(data.get("file_id", 0)),
            mime=str(data.get("mime")),
            dc_id=int(data.get("dc_id", 0)),
            access_hash_rec=str(data.get("access_hash_rec")),
            file_name=str(data.get("file_name")),
            thumb_inline=str(data.get("thumb_inline")),
            width=int(data.get("width", 0)),
            height=int(data.get("height", 0)),
            time=int(data.get("time", 0)),
            size=int(data.get("size", 0)),
            type=FileType(data.get("type")) if data.get("type") else None,
            music_performer=data.get("music_performer"),
            is_round=bool(data.get("is_round")),
            is_spoil=bool(data.get("is_spoil")),
            raw=data,
        )
