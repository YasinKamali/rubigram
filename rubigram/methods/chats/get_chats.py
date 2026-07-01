from typing import Optional

import rubigram


class GetChats:
    async def get_chats(
        self: "rubigram.Client",
        start_id: Optional[str] = None,
    ) -> ...:
        return await self.invoke("getChats", {"start_id": start_id})