from typing import Any
from dataclasses import dataclass

from rubigram.types import Base, Chat, User, OnlineTime, FileInline


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


@dataclass()
class Color(Base):
    alpha: int
    blue: int
    green: int
    red: int

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Color":
        data.update(**kwargs)
        return cls(
            alpha=data.get("alpha"),
            blue=data.get("blue"),
            green=data.get("green"),
            red=data.get("red")
        )


@dataclass()
class Warning(Base):
    link: ...
    text: str
    title: str
    title_color: "Color"
    warning_id: str

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Color":
        data.update(**kwargs)
        return cls(
            link=data.get("link"),
            text=data.get("text"),
            title=data.get("title"),
            title_color=Color.read(
                data["title_color"] if data.get("title_color") else None
            ),
            warning_id=data.get("warning_id")
        )


@dataclass()
class UserAdditionalInfo(Base):
    can_receive_call: bool
    can_video_call: bool
    count_common_groups: int
    country_code: str
    is_in_contact: bool
    name_changed_time: int
    official_info_text: str
    photo_changed_time: int
    registration_time: int

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Color":
        data.update(**kwargs)
        return cls(
            can_receive_call=data.get("can_receive_call"),
            count_common_groups=data.get("count_common_groups"),
            can_video_call=data.get("can_video_call"),
            country_code=data.get("country_code"),
            is_in_contact=data.get("is_in_contact"),
            name_changed_time=data.get("name_changed_time"),
            official_info_text=data.get("official_info_text"),
            photo_changed_time=data.get("photo_changed_time"),
            registration_time=data.get("registration_time")
        )


@dataclass()
class UserInfo(Base):
    chat: "Chat"
    timestamp: int
    user: "User"
    user_additional_info: "UserAdditionalInfo"

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "UserInfo":
        data.update(**kwargs)
        return cls(
            chat=Chat.read(data["chat"]) if data.get("chat") else None,
            timestamp=data.get("timestamp"),
            user=User.read(data["user"]) if data.get("user") else None,
            user_additional_info=UserAdditionalInfo.read(
                data["user_additional_info"]
                if data.get("user_additional_info") else None
            )
        )