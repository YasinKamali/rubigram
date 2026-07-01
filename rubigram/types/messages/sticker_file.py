from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field


@dataclass()
class StickerFile(Base):
    file_id: str
    mime: str
    dc_id: str
    access_hash_rec: str
    file_name: str
    cdn_tag: str
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "StickerFile":
        data.update(kwargs)
        return cls(
            file_id=str(data.get("file_id")),
            mime=str(data.get("mime")),
            dc_id=str(data.get("dc_id")),
            access_hash_rec=str(data.get("access_hash_rec")),
            file_name=str(data.get("file_name")),
            cdn_tag=str(data.get("cdn_tag")),
            raw=data,
        )
