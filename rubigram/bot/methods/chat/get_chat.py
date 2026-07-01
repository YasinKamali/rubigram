#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram
from rubigram.bot.types import Chat


class GetChat:
    async def get_chat(
        self: "rubigram.Bot",
        chat_id: str,
    ) -> "Chat":
        """Get up to date information about a chat.

        Args:
            chat_id (`str`): The unique ID of the chat.

        Returns:
            `rubigram.types.Chat`

        Example:
        .. code-block:: python
            await bot.get_chat(chat_id="chat_id")
        """
        response = await self.invoke("getChat", {"chat_id": chat_id})
        return Chat.read(response["chat"])