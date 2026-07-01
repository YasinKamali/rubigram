import rubigram


class GetJoinRequests:
    async def get_join_requests(
        self: "rubigram.Client",
        guid: str
    ) -> dict:
        return await self.invoke("getJoinRequests", input={"object_guid": guid})