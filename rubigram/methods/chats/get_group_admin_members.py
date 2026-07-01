import rubigram



class GetGroupAdminMembers:
    async def get_group_admin_members(
        self: "rubigram.Client",
        group_guid: str,
        start_id: str = None,
    ):
        return await self.invoke("getGroupAdminMembers", {
            "group_guid": group_guid,
            "start_id": start_id,
        })