#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram


class GetChatMember:
    async def get_chat_member(
        self: "rubigram.Bot",
        chat_id: str,
        user_id: str,
    ) -> "rubigram.types.Chat":
        """Get information about one member of a chat.

        Args:
            chat_id (`str`): The unique ID of the chat.
            user_id (`str`): The unique ID of the user.

        Returns:
            `rubigram.types.Chat`
        
        Example:
        .. code-block:: python
            await bot.get_chat_member(chat_id="chat_id", user_id="user_id")
        """
        return await self.invoke("GetChatMember", {"chat_id": chat_id, "user_id": user_id})