import rubigram


class GetBannedGroupMembers:
    async def get_banned_group_members(
        self: "rubigram.Client",
        group_guid: str,
        start_id: str = None,
    ):
        return await self.invoke("getBannedGroupMembers", {
            "group_guid": group_guid,
            "start_id": start_id,
        })