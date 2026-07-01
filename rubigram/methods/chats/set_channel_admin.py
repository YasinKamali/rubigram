from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, Union, Any

import rubigram


ACCESS_LIST = [
    "SetAdmin"
    "AddMember",
    "ChangeInfo",
    "ViewAdmins",
    "SetJoinLink",
    "ViewMembers",
    "PinMessages",
    "SendMessages",
    "EditAllMessages",
    "DeleteGlobalAllMessages",
]


class AdminAction(Enum):
    SetAdmin = auto()
    UnsetAdmin = auto()


@dataclass
class ChannelAccess:
    set_admin: bool = False
    add_member: bool = False
    change_info: bool = False
    view_admins: bool = False
    view_members: bool = False
    pin_messages: bool = False
    send_messages: bool = False
    set_join_link: bool = False
    edit_all_messages: bool = False
    delete_global_all_messages: bool = False

    def write(self) -> Union[list[str], None]:
        access_list = []

        for name, status in self.__dict__.items():
            if status:
                access = "".join([i.capitalize() for i in name.split("_")])
                access_list.append(access)

        return access_list if access_list else None

    def read(cls, data: dict[str, Any]) -> "ChannelAccess":
        return cls(
            ...
        )

    @classmethod
    def all(cls) -> list[str]:
        return ACCESS_LIST


class SetChannelAdmin:
    async def set_channel_admin(
        self: "rubigram.Client",
        channel_guid: str,
        member_guid: str,
        access_list: Optional["ChannelAccess"] = None,
        action: AdminAction = AdminAction.SetAdmin,
    ):
        if not isinstance(action, AdminAction):
            raise ValueError()

        if isinstance(access_list, ChannelAccess):
            access_list = access_list.write()

        return await self.invoke("setChannelAdmin", {
            "channel_guid": channel_guid,
            "member_guid": member_guid,
            "action": action.name,
            "access_list": access_list
        })

    async def unset_channel_admin(
        self: "rubigram.Client",
        channel_guid: str,
        member_guid: str
    ):
        return await self.set_channel_admin(channel_guid, member_guid, action=AdminAction.UnsetAdmin)