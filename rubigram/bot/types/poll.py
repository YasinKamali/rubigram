#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base
from rubigram.bot.types import PollStatus

from dataclasses import dataclass


@dataclass()
class Poll(Base):
    question: Optional[str] = None
    options: Optional[list[str]] = None
    poll_status: Optional["PollStatus"] = None

    def write(self) -> dict[str, Any]:
        poll_status = self.poll_status.write() if self.poll_status else None
        return {
            "question": self.question,
            "options": self.options,
            "poll_status": poll_status
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "Poll":
        poll_status = data.get("poll_status")
        return cls(
            question=data.get("question"),
            options=data.get("options"),
            poll_status=PollStatus.read(poll_status) if poll_status else None
        )