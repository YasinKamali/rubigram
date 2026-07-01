#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram
from rubigram.bot.types import Bot


class GetMe:
    async def get_me(self: "rubigram.Bot") -> "Bot":
        """Get current bot information.

        Parameters:
            `None`

        Returns:
            `rubigram.types.Bot`

        Example:
        .. code-block:: python
            me = await client.get_me()
            print(me)
        """
        response = await self.invoke("getMe")
        return Bot.read(response["bot_info"])