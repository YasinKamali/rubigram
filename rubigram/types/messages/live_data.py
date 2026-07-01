from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field
from .live_status import LiveStatus


@dataclass()
class LiveData(Base):
    live_id: str
    thumb_inline: str
    access_token: str
    live_status: "LiveStatus"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "LiveData":
        data.update(kwargs)
        return cls(
            live_id=str(data.get("live_id")),
            thumb_inline=str(data.get("thumb_inline")),
            access_token=str(data.get("access_token")),
            live_status=LiveStatus.read(data.get("live_status", {})),
            raw=data,
        )
