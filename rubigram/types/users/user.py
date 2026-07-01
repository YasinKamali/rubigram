from typing import Optional, Any
from dataclasses import dataclass, field

from rubigram.types import Base
# from rubigram.types import FileInline, OnlineTime, MessageInfo, Badge, Story, Warning
from ..messages import FileInline, MessageInfo, Badge
from ..online_time import OnlineTime
from ..stories import Story
from ..warnings import Warning


@dataclass()
class User(Base):
    avatar_thumbnail: Optional["FileInline"]
    badge: Optional["Badge"]
    bio: Optional[str]
    birth_date: Optional[str]
    first_name: str
    last_name: Optional[str]
    is_deleted: bool
    is_verified: bool
    last_online: int
    message_info: Optional["MessageInfo"]
    online_time: "OnlineTime"
    phone: str
    saved_music_last_track: Optional["FileInline"]
    story: Optional["Story"]
    timestamp: int
    user_guid: str
    username: Optional[str]
    warning_info: Optional["Warning"]
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "User":
        data.update(**kwargs)
        return cls(
            avatar_thumbnail=FileInline.read(data["avatar_thumbnail"]) if data.get(
                "avatar_thumbnail") else None,
            badge=Badge.read(data["badge"]) if data.get("badge") else None,
            bio=data.get("bio"),
            birth_date=data.get("birth_date"),
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name"),
            is_deleted=bool(data.get("is_deleted")),
            is_verified=bool(data.get("is_verified")),
            last_online=data.get("last_online", 0),
            message_info=MessageInfo.read(
                data["message_info"]) if data.get("message_info") else None,
            online_time=OnlineTime.read(data["online_time"]),
            phone=str(data.get("phone")),
            saved_music_last_track=FileInline.read(
                data["saved_music_last_track"]) if data.get("saved_music_last_track") else None,
            story=Story.read(data["story"]) if data.get("story") else None,
            timestamp=data.get("timestamp", 0),
            user_guid=str(data.get("user_guid")),
            username=data.get("username"),
            warning_info=Warning.read(data["warning_info"]) if data.get(
                "warning_info") else None,
            raw=data
        )