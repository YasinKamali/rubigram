from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field
from rubigram.enums import LiveStatusType


@dataclass()
class LiveStatus(Base):
    status: "LiveStatusType"
    allow_comment: bool
    can_play: bool
    timestamp: str
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "LiveStatus":
        data.update(kwargs)
        return cls(
            status=LiveStatusType(data.get("status")),
            allow_comment=bool(data.get("allow_comment")),
            can_play=bool(data.get("can_play")),
            timestamp=str(data.get("timestamp")),
            raw=data,
        )
