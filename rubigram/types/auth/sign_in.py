from typing import Any, Optional
from dataclasses import dataclass, field

import rubigram
from ..base import Base
from rubigram.enums import SignInStatus
from ..users import User


@dataclass()
class SignIn(Base):
    auth: Optional[str]
    timestamp: Optional[int]
    status: Optional["SignInStatus"]
    user: Optional["User"]
    client: "rubigram.Client"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "SignIn":
        data.update(kwargs)
        status = data.get("status")
        return cls(
            auth=data.get("auth"),
            timestamp=data.get("timestamp"),
            status=SignInStatus(status) if status else None,
            user=User.read(data.get("user")) if data.get("user") else None,
            client=data.get("client"),
            raw=data
        )

    @property
    def decode_auth(cls) -> str:
        return cls.client.crypto.decrypt_RSA_OAEP(cls.client.private_key, cls.auth)

    async def sign_in(
        self,
        phone_code: str,
    ):

        if not self.client:
            raise RuntimeError("Client is not set for this SentCode instance.")

        if not self.phone_number:
            raise RuntimeError(
                "phone_number is not set for this SentCode instance."
            )

        if not self.phone_code_hash:
            raise RuntimeError(
                "phone_code_hash is not set for this SentCode instance."
            )

        return await self.client.sign_in(
            phone_number=self.phone_number,
            phone_code=phone_code,
            phone_code_hash=self.phone_code_hash
        )