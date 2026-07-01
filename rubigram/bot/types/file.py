#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import mimetypes
from typing import Optional, Any

from .base import Base
from rubigram.bot.enums import FileType

from dataclasses import dataclass


@dataclass()
class File(Base):
    file_id: str
    file_name: Optional[str] = None
    size: Optional[int] = None
    type: Optional["FileType"] = None

    def write(self) -> dict[str, Any]:
        return {
            "file_id": self.file_id,
            "file_name": self.file_name,
            "size": self.size,
            "type": self.type,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "File":
        type = data.get("type")
        return cls(
            file_id=data.get("file_id"),
            file_name=data.get("file_name"),
            size=data.get("size"),
            type=FileType(type) if type else None
        )

    def __post_init__(self):
        if not self.file_name:
            self.type = FileType.FILE
            return

        mime_type, _ = mimetypes.guess_type(self.file_name)
        if not mime_type:
            self.type = FileType.FILE
            return

        mime_main = mime_type.split("/")[0]
        mime_sub = mime_type.split("/")[1]

        if mime_main == "image":

            if mime_sub == "gif":
                self.type = FileType.GIF

            else:
                self.type = FileType.IMAGE

        elif mime_main == "video":
            self.type = FileType.VIDEO

        elif mime_main == "audio":

            if mime_sub in ["ogg", "amr", "m4a"]:
                self.type = FileType.VOICE

            else:
                self.type = FileType.MUSIC

        else:
            self.type = FileType.FILE