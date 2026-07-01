#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigra


from typing import Optional

import rubigram
from rubigram.bot.types import Updates


class GetUpdates:
    async def get_updates(
        self: "rubigram.Bot",
        limit: int = 1,
        offset_id: Optional[str] = None
    ) -> "Updates":
        response = await self.invoke("getUpdates", {"limit": limit, "offset_id": offset_id})
        if response:
            return Updates.read(response)
        else:
            return Updates()