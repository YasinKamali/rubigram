#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any

from ..base import Base
from .button_selection_item import ButtonSelectionItem

from dataclasses import dataclass


@dataclass()
class ButtonSelection(Base):
    selection_id: Optional[str] = None
    search_type: Optional[str] = None
    get_type: Optional[str] = None
    items: Optional[list["ButtonSelectionItem"]] = None
    is_multi_selection: Optional[bool] = None
    columns_count: Optional[str] = None
    title: Optional[str] = None

    def write(self) -> dict[str, Any]:
        return {
            "selection_id": self.selection_id,
            "search_type": self.search_type,
            "get_type": self.get_type,
            "items": ...,
            "is_multi_selection": self.is_multi_selection,
            "columns_count": self.columns_count,
            "title": self.title
        }

    @classmethod
    def read(cls, data: dict[str, Any]) -> "ButtonSelection":
        ...