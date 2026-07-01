import rubigram
from typing import Literal


class ActionOnJoinRequest:
    async def action_on_join_request(
        self: "rubigram.Client",
        object_guid: str,
        user_guid: str,
        action: Literal["Accept", "Reject"] = "Accept"
    ) -> ...:

        object_type = "Group" if object_guid.startswith("g0") else "Channel"

        return await self.invoke("actionOnJoinRequest", {
            "object_guid": object_guid,
            "object_type": object_type,
            "user_guid": user_guid,
            "action": action,
        })