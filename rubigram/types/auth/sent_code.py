from typing import Any, Optional, Union
from dataclasses import dataclass, field

import rubigram
from rubigram.types.auth.sign_in import SignIn
from ..base import Base
from rubigram.enums import SentCodeType, SentCodeStatus


# @dataclass()
# class SentCode(Base):
#     client: Optional["rubigram.Client"] = field(default=None, repr=False)
#     status: Optional["SentCodeStatus"] = None
#     hint_pass_key: Optional[str] = None
#     phone_code_hash: Optional[str] = None
#     code_digits_count: Optional[int] = None
#     has_recovery_email: Optional[bool] = None
#     type: Optional["SentCodeType"] = None
#     phone_number: Optional[str] = None
#     raw : dict = field(repr=False)
@dataclass()
class SentCode(Base):
    phone_number: Optional[str]
    code_digits_count: Optional[int]
    has_confirmed_recovery_email: bool
    no_recovery_alert: Optional[str]
    hint_pass_key: Optional[str]
    phone_code_hash: Optional[str]
    status: Optional["SentCodeStatus"]
    send_type: Optional["SentCodeType"]
    client: "rubigram.Client"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "SentCode":
        data.update(kwargs)
        return cls(
            phone_number=data.get("phone_number"),
            code_digits_count=data.get("code_digits_count"),
            has_confirmed_recovery_email=bool(
                data.get("has_confirmed_recovery_email")),
            hint_pass_key=data.get("hint_pass_key"),
            no_recovery_alert=data.get("no_recovery_alert"),
            phone_code_hash=data.get("phone_code_hash"),
            status=SentCodeStatus(data.get("status")) if data.get(
                "status") else None,
            send_type=SentCodeType(data.get("send_type")) if data.get(
                "send_type") else None,
            client=data.get("client"),
            raw=data
        )

    async def sign_in(
        self,
        phone_code: str,
    ) -> SignIn:

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