#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from .base import Base
from rubigram.bot.enums import PollStatusType

from dataclasses import dataclass


@dataclass()
class PollStatus(Base):
    state: Optional[PollStatusType] = None
    selection_index: Optional[int] = None
    percent_vote_options: Optional[list[int]] = None
    total_vote: Optional[int] = None
    show_total_votes: Optional[bool] = None

    def write(self) -> dict[str, Any]:
        return {
            "state": self.state.value,
            "selection_index": self.selection_index,
            "percent_vote_options": self.percent_vote_options,
            "total_vote": self.total_vote,
            "show_total_votes": self.show_total_votes,
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "PollStatus":
        state = data.get("state")
        return cls(
            state=PollStatusType(state) if state else None,
            selection_index=data.get("selection_index"),
            percent_vote_options=data.get("percent_vote_options"),
            total_vote=data.get("total_vote"),
            show_total_votes=data.get("show_total_votes")
        )