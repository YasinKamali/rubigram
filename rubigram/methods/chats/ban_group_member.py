import rubigram
from typing import Literal


class BanGroupMember:
    async def ban_group_member(
        self: "rubigram.Client",
        group_guid: str,
        member_guid: str,
        action: Literal["Set", "Unset"] = "Set",
    ) -> ...:
        return await self.invoke("banGroupMember", {
            "group_guid": group_guid,
            "member_guid": member_guid,
            "action": action,
        })

    async def unban_group_member(
        self: "rubigram.Client",
        group_guid: str,
        member_guid: str
    ):
        return await self.ban_group_member(group_guid, member_guid, "Unset")