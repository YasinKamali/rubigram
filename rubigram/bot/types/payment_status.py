#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from __future__ import annotations
from typing import Optional, Any

from .base import Base
from rubigram.bot.enums import PaymentStatusType

from dataclasses import dataclass


@dataclass()
class PaymentStatus(Base):
    payment_id: Optional[str] = None
    status: Optional["PaymentStatusType"] = None

    def write(self) -> dict[str, Any]:
        return {
            "start_id": self.payment_id,
            "status": self.status.value,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "PaymentStatus":
        status = data.get("status")
        return cls(
            payment_id=data.get("payment_id"),
            status=PaymentStatusType(status) if status else None
        )