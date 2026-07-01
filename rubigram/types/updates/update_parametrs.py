from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field


@dataclass()
class UpdatedParameters(Base):
    last_message_id: bool
    last_message: bool
    status: bool
    time_string: bool
    count_unseen: bool
    last_seen_peer_mid: bool
    time: bool
    raw: list = field(repr=False)

    @classmethod
    def read(cls, data: list[str]) -> "UpdatedParameters":
        return cls(
            last_message_id="last_message_id" in data,
            last_message="last_message" in data,
            status="status" in data,
            time_string="time_string" in data,
            count_unseen="count_unseen" in data,
            last_seen_peer_mid="last_seen_peer_mid" in data,
            time="time" in data,
            raw=data,
        )
