from dataclasses import dataclass
from typing import Optional, Any
from rubigram.types.base import Base


@dataclass()
class Story(Base):
    last_story_time: int
    profile_id: str

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Story":
        data.update(**kwargs)
        return cls(
            last_story_time=data.get("last_story_time"),
            profile_id=data.get("profile_id")
        )
