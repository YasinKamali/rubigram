import rubigram


class GetGroupLink:
    async def get_group_link(
        self: "rubigram.Client",
        group_guid: str,
    ):
        return await self.invoke("getGroupLink", {"group_guid": group_guid})