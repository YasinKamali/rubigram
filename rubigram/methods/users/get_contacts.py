import rubigram
from typing import Optional


class GetContacts:
    async def get_contacts(
        self: "rubigram.Client",
        start_id: Optional[str] = None,
    ):
        return await self.invoke("getContacts", {
            "start_id": start_id
        })