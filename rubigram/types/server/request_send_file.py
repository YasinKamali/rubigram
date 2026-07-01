from typing import Optional, Any
from dataclasses import dataclass

from rubigram.types import Base


@dataclass()
class RequestSendFileResult(Base):
    id: str
    dc_id: str
    upload_url: str
    access_hash_send: str
    size: Optional[int] = None
    mime: Optional[str] = None
    name: Optional[str] = None
    file: Optional[bytes] = None
    access_hash_rec: Optional[str] = None

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "RequestSendFileResult":
        data.update(**kwargs)
        return cls(
            id=data.get("id"),
            dc_id=data.get("dc_id"),
            upload_url=data.get("upload_url"),
            access_hash_send=data.get("access_hash_send"),
            size=data.get("size"),
            mime=data.get("mime"),
            name=data.get("name"),
            file=data.get("file"),
            access_hash_rec=data.get("access_hash_rec")
        )