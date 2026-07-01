from typing import Any, Optional, List
from dataclasses import dataclass, field

import rubigram
from ..base import Base
from rubigram.enums import SignInStatus


@dataclass()
class Session(Base):
    app_brand: str
    app_type: str
    app_version: str
    device: str
    ip: str
    isCurrentSession: bool
    key: str
    last_access: str
    location: str
    login_time: int
    terminatable: bool
    client: "rubigram.Client"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Session":
        data.update(kwargs)
        return cls(
            app_brand=data.get("app_brand"),
            app_type=data.get("app_type"),
            app_version=data.get("app_version"),
            device=data.get("device"),
            ip=data.get("ip"),
            isCurrentSession=bool(data.get("isCurrentSession")),
            key=data.get("key"),
            last_access=data.get("last_access"),
            location=data.get("location"),
            login_time=int(data.get("login_time", 0)),
            terminatable=bool(data.get("terminatable")),
            client=data.get("client"),
            raw=data
        )

    @property
    def decode_auth(cls) -> str:
        return cls.client.session.crypto.decrypt_RSA_OAEP(cls.client.session.private_key, cls.auth)

    async def sign_in(
        self,
        phone_code: str,
    ):

        if not self.client:
            raise RuntimeError("Client is not set for this SentCode instance.")

        if not self.phone_number:
            raise RuntimeError(
                "phone_number is not set for this SentCode instance.")

        if not self.phone_code_hash:
            raise RuntimeError(
                "phone_code_hash is not set for this SentCode instance.")

        return await self.client.sign_in(
            phone_number=self.phone_number,
            phone_code=phone_code,
            phone_code_hash=self.phone_code_hash
        )
