#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram
from rubigram.bot.enums import UpdateEndpointType


class UpdateBotEndpoints:
    async def update_bot_endpoints(
        self: "rubigram.Bot",
        url: str,
        type: "UpdateEndpointType" = UpdateEndpointType.RECEIVE_UPDATE,
    ) -> dict:
        return await self.invoke("updateBotEndpoints", {"url": url, "type": type.value})