#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram


class BanChatMember:
    async def ban_chat_member(
        self: "rubigram.Bot",
        chat_id: str,
        user_id: str
    ) -> "rubigram.types.Chat":
        """Ban a user.

        Parameters:
            chat_id (`str`): The unique ID of the chat.
            user_id (`str`): The unique ID of the user.

        Returns:
            `rubigram.types.Chat`
            
        Example:
        .. code-block:: python
            await bot.ban_chat_member(chat_id="chat_id", user_id="user_id")
        """
        return await self.invoke("banChatMember", {"chat_id": chat_id, "user_id": user_id})