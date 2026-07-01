# rubigram/ask.py

import asyncio
import rubigram
from typing import Optional, Union, List, Any, Callable
from datetime import datetime

from rubigram.filters import Filter
from rubigram import filters
from rubigram.types import Update


class AskManager:
    """
    Ask manager for handling interactive conversations with users
    Compatible with Rubigram's existing Storage and State system
    """
    
    def __init__(self, client:"rubigram.Client"):
        self.client = client
        self._pending_asks: dict[str, asyncio.Future] = {}
        self._pending_filters: dict[str, Optional[Filter]] = {}
        self._default_timeout = 60
        
        # Register internal handler
        self._register_handler()
    
    def _register_handler(self):
        """Register internal handler to catch user responses"""
        
        @self.client.on_message(group=-999)  # Highest priority
        async def _ask_response_handler(client, update: Update):
            user_id = str(update.message.author_object_guid)
            
            if user_id in self._pending_asks:
                future = self._pending_asks[user_id]
                answer_filter = self._pending_filters.get(user_id)
                
                # Check if message passes the filter
                if answer_filter is not None:
                    if not await self._check_filter(client,answer_filter, update):
                        return False  # Don't consume, let other handlers process
                
                if not future.done():
                    future.set_result(update)
                    del self._pending_asks[user_id]
                    del self._pending_filters[user_id]
                    return True  # Consumed by ask handler
            
            return False
    
    async def _check_filter(self,client, filter_obj: Filter, update: Update) -> bool:
        """Check if update passes the filter"""
        if callable(filter_obj):
            result = filter_obj(client, update)
            if asyncio.iscoroutine(result):
                return await result
            return result
        return True
    
    async def ask(
        self,
        user_id: Union[str, int],
        question: str,
        timeout: Optional[int] = None,
        filters: Optional[Filter] = None,
        parse_mode: Optional[str] = None,
        reply_to_message_id: Optional[str] = None,
        **kwargs
    ) -> Update:
        """
        Send a question to user and wait for response
        
        Args:
            user_id: User's GUID or ID
            question: Question text to send
            timeout: Timeout in seconds (None = infinite)
            filters: Filter for response (e.g., filters.text, filters.photo)
            parse_mode: Parse mode for question message
            reply_to_message_id: Reply to specific message
            **kwargs: Additional arguments for send_message
        
        Returns:
            Update object containing user's response
        
        Raises:
            TimeoutError: If user doesn't respond within timeout
        """
        user_id = str(user_id)
        
        # Create future for waiting
        future = asyncio.Future()
        
        # Store pending ask
        self._pending_asks[user_id] = future
        self._pending_filters[user_id] = filters
        
        # Send question
        x = await self.client.send_message(
            user_id,
            question,
            parse_mode=parse_mode,
            reply_to_message_id=reply_to_message_id,
            **kwargs
        )
        
        # Handle timeout
        timeout_seconds = timeout if timeout is not None else self._default_timeout
        
        try:
            if timeout_seconds > 0:
                response = await asyncio.wait_for(future, timeout=timeout_seconds)
            else:
                response = await future
            return response
        except asyncio.TimeoutError:
            raise TimeoutError(f"No response received from user {user_id} within {timeout_seconds} seconds")
        finally:
            # Cleanup
            self._pending_asks.pop(user_id, None)
            self._pending_filters.pop(user_id, None)
    
    def is_waiting(self, user_id: Union[str, int]) -> bool:
        """Check if user has a pending ask"""
        return str(user_id) in self._pending_asks
    
    def cancel(self, user_id: Union[str, int]) -> bool:
        """Cancel pending ask for a user"""
        user_id = str(user_id)
        if user_id in self._pending_asks:
            self._pending_asks[user_id].cancel()
            del self._pending_asks[user_id]
            self._pending_filters.pop(user_id, None)
            return True
        return False


# Mixin to add to Client class
class AskMixin:
    """Mixin to add ask functionality to Client"""
    
    @property
    def ask(self) -> AskManager:
        """Get ask manager instance"""
        if not hasattr(self, '_ask_manager'):
            self._ask_manager = AskManager(self)
        return self._ask_manager