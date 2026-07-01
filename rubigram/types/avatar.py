from typing import Optional, Any
from dataclasses import dataclass


@dataclass
class Avatar:
    file_id: Optional[str] = None
    mime: Optional[str] = None
    dc_id: Optional[str] = None
    access_hash_rec: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "file_id": self.file_id,
            "mime": self.mime,
            "dc_id": self.dc_id,
            "access_hash_rec": self.access_hash_rec
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Avatar":
        return cls(
            file_id=data.get("file_id"),
            mime=data.get("mime"),
            dc_id=data.get("dc_id"),
            access_hash_rec=data.get("access_hash_rec")
        )