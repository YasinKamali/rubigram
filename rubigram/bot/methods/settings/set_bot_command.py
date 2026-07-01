#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Union

import rubigram
from rubigram.bot.types import BotCommand


class SetBotCommand:
    async def set_bot_command(
        self: "rubigram.Bot",
        command: Union["BotCommand", list["BotCommand"]],
    ) -> dict:
        if isinstance(command, BotCommand):
            command = [command]

        return await self.invoke("setCommands", {"bot_commands": [c.write() for c in command]})