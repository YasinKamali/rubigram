from typing import Any
from dataclasses import dataclass

from rubigram.types import Base


@dataclass()
class UploadfileResult(Base):
    ...

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "UploadfileResult":
        data.update(**kwargs)
        return cls(
            
        )