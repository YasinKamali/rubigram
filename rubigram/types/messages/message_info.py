from dataclasses import dataclass
from typing import Optional, Any
from rubigram.types.base import Base
from .file_inline import FileInline



@dataclass()
class MessageInfo(Base):
    button_text: str
    label_detail: str
    label_main: str
    link: ...
    message_info_id: str
    photo: "FileInline"
    text: str
    title: str

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "MessageInfo":
        data.update(**kwargs)
        return cls(
            button_text=data.get("button_text"),
            label_detail=data.get("label_detail"),
            label_main=data.get("label_main"),
            link=data.get("link"),
            message_info_id=data.get("message_info_id"),
            photo=FileInline.read(
                data["photo"] if data.get("photo") else None
            ),
            text=data.get("text"),
            title=data.get("title")
        )