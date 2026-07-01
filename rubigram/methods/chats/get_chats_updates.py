import time
import rubigram
from typing import Optional


class GetChatsUpdates:
    async def get_chats_updates(
        self: "rubigram.Client",
        state: Optional[int] = None
    ) -> ...:
        return await self.invoke("getChatsUpdates", {
            "state": round(time.time()) - 150 if not state else int(state)
        })