from ..base import Base
from typing import Any
from dataclasses import dataclass, field


@dataclass()
class ContactMessage(Base):
    phone_number: str
    first_name: str
    last_name: str
    user_guid: str
    vcard: str
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "ContactMessage":
        data.update(kwargs)
        return cls(
            phone_number=str(data.get("phone_number")),
            first_name=str(data.get("first_name")),
            last_name=str(data.get("last_name")),
            user_guid=str(data.get("user_guid")),
            vcard=str(data.get("vcard")),
            raw=data,
        )
