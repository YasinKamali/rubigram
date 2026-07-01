from typing import Any, Optional,List
from dataclasses import dataclass, field

import rubigram
from ..base import Base
from .session import Session


@dataclass()
class SessionInfo(Base):
    active_session: Session
    can_remove_all: bool
    other_sessions: List[Session]
    _client: "rubigram.Client"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "SessionInfo":
        data.update(kwargs)
        return cls(
            active_session = Session.read(data.get("active_session")),
            can_remove_all = bool(data.get("can_remove_all")),
            other_sessions = [Session.read(session_data) for session_data in data.get("other_sessions",[])],
            _client = data.get("client"),
            raw = data
        )

