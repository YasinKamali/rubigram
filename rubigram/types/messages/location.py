from rubigram.types.base import Base
from typing import Any
from dataclasses import dataclass, field
from .map_view import MapView


@dataclass()
class Location(Base):
    longitude: float
    latitude: float
    map_view: "MapView"
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Location":
        data.update(kwargs)
        return cls(
            longitude=float(data.get("longitude", 0)),
            latitude=float(data.get("latitude", 0)),
            map_view=MapView.read(data.get("map_view", {})),
            raw=data,
        )
