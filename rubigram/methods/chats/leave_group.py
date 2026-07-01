import rubigram


class LeaveGroup:
    async def leave_group(
        self: "rubigram.Client",
        guid: str,
    ) -> ...:
        """Leave from the group.

        Args:
            guid (str): GUID of the group
        """
        return await self.invoke("leaveGroup", input={"group_guid": guid})