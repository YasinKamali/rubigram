from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field


@dataclass()
class RubinoPost(Base):
    post_id: str
    post_profile_id: str
    track_id: str
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "RubinoPost":
        data.update(kwargs)
        return cls(
            post_id=str(data.get("post_id")),
            post_profile_id=str(data.get("post_profile_id")),
            track_id=str(data.get("track_id")),
            raw=data,
        )
