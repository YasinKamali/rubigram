from enum import Enum, auto

import rubigram


class JoinChannelAction(Enum):
    Join = auto()
    Leave = auto()
    Remove = auto()
    Archive = auto()


class JoinChannel:
    async def join_channel(
        self: "rubigram.Client",
        guid: str,
        action: JoinChannelAction = JoinChannelAction.Join,
    ) -> ...:

        return await self.invoke("joinChannelAction", {
            "channel_guid": guid,
            "action": action.name
        })

    async def leave_channel(
        self: "rubigram.Client",
        guid: str
    ) -> ...:
        return await self.join_channel(guid, JoinChannelAction.Leave)