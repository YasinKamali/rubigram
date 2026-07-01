from rubigram.types.base.base import Base
from typing import Any
from dataclasses import dataclass, field


@dataclass()
class MapView(Base):
    tile_side_count: int
    tile_urls: list[str]
    x_loc: float
    y_loc: float
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "MapView":
        data.update(kwargs)
        return cls(
            tile_side_count=int(data.get("tile_side_count", 0)),
            tile_urls=[url for url in data.get("tile_urls", [])],
            x_loc=float(data.get("x_loc", 0)),
            y_loc=float(data.get("y_loc", 0)),
            raw=data,
        )
