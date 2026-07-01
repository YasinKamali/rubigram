from typing import Optional, Any
from dataclasses import dataclass
from rubigram.enums import OnlineTimeType


@dataclass
class OnlineTime:
    type: Optional["OnlineTimeType"] = None
    exact_time: Optional[int] = None
    approximate_period: Optional[str] = None

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "OnlineTime":
        data.update(**kwargs)
        return cls(
            type=OnlineTimeType(data.get("type")) if data.get(
                "type") else None,
            exact_time=data.get("exact_time"),
            approximate_period=data.get("approximate_period")
        )