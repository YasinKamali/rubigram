# rubigram/listener.py

import asyncio
from inspect import iscoroutinefunction
from typing import Optional, Callable, Dict, List, Union, Any
from dataclasses import dataclass, field
from enum import Enum

from rubigram.filters import Filter
from rubigram.types import Update


class ListenerTypes(Enum):
    MESSAGE = "message"
    CALLBACK_QUERY = "callback_query"
    INLINE_QUERY = "inline_query"
    EDITED_MESSAGE = "edited_message"


@dataclass
class Identifier:
    """Identifies a specific update pattern"""
    from_user_id: Optional[Union[str, List[str]]] = None
    chat_id: Optional[Union[str, List[str]]] = None
    message_id: Optional[Union[str, List[str]]] = None
    inline_message_id: Optional[Union[str, List[str]]] = None

    def matches(self, other: "Identifier") -> bool:
        """Check if this identifier matches another"""
        if self.from_user_id is not None:
            if isinstance(self.from_user_id, list):
                if other.from_user_id not in self.from_user_id:
                    return False
            elif self.from_user_id != other.from_user_id:
                return False

        if self.chat_id is not None:
            if isinstance(self.chat_id, list):
                if other.chat_id not in self.chat_id:
                    return False
            elif self.chat_id != other.chat_id:
                return False

        if self.message_id is not None:
            if isinstance(self.message_id, list):
                if other.message_id not in self.message_id:
                    return False
            elif self.message_id != other.message_id:
                return False

        if self.inline_message_id is not None:
            if isinstance(self.inline_message_id, list):
                if other.inline_message_id not in self.inline_message_id:
                    return False
            elif self.inline_message_id != other.inline_message_id:
                return False

        return True

    def count_populated(self) -> int:
        """Count how many fields are populated (for priority sorting)"""
        count = 0
        if self.from_user_id is not None:
            count += 1
        if self.chat_id is not None:
            count += 1
        if self.message_id is not None:
            count += 1
        if self.inline_message_id is not None:
            count += 1
        return count


@dataclass
class Listener:
    """Represents a waiting listener"""
    future: Optional[asyncio.Future] = None
    callback: Optional[Callable] = None
    filters: Optional[Filter] = None
    unallowed_click_alert: bool = True
    identifier: Optional[Identifier] = None
    listener_type: ListenerTypes = ListenerTypes.MESSAGE
    sent_message: Any = None

    def __post_init__(self):
        if self.future is None and self.callback is None:
            raise ValueError("Either future or callback must be provided")


class ListenerManager:
    """Manages all listeners for a client"""

    def __init__(self, client):
        self.client = client
        self.listeners: Dict[ListenerTypes, List[Listener]] = {
            listener_type: [] for listener_type in ListenerTypes
        }

    def add(self, listener: Listener):
        """Add a listener"""
        self.listeners[listener.listener_type].append(listener)

    def remove(self, listener: Listener):
        """Remove a listener"""
        try:
            self.listeners[listener.listener_type].remove(listener)
        except ValueError:
            pass

    def find_matching(
        self,
        data: Identifier,
        listener_type: ListenerTypes
    ) -> Optional[Listener]:
        """Find the most specific matching listener"""
        matching = []
        for listener in self.listeners[listener_type]:
            if listener.identifier and listener.identifier.matches(data):
                matching.append(listener)

        if not matching:
            return None

        # Return the most specific (most populated fields)
        return max(matching, key=lambda l: l.identifier.count_populated())

    def find_all_matching(
        self,
        pattern: Identifier,
        listener_type: ListenerTypes
    ) -> List[Listener]:
        """Find all matching listeners"""
        matching = []
        for listener in self.listeners[listener_type]:
            if pattern.matches(listener.identifier):
                matching.append(listener)
        return matching

    async def stop_all(
        self,
        listener_type: ListenerTypes,
        chat_id: Optional[Union[str, List[str]]] = None,
        user_id: Optional[Union[str, List[str]]] = None,
        message_id: Optional[Union[str, List[str]]] = None,
        inline_message_id: Optional[Union[str, List[str]]] = None
    ):
        """Stop all matching listeners"""
        pattern = Identifier(
            from_user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id
        )

        listeners = self.find_all_matching(pattern, listener_type)
        for listener in listeners:
            await self.stop_one(listener)

    async def stop_one(self, listener: Listener):
        """Stop a single listener"""
        self.remove(listener)

        if listener.future and not listener.future.done():
            listener.future.set_exception(Exception("Listener stopped"))