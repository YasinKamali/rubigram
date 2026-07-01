from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, Union, Any

import rubigram


ACCESS_LIST = [
    "SetAdmin",
    "BanMember",
    "ChangeInfo",
    "PinMessages",
    "SetJoinLink",
    "SetMemberAccess",
    "DeleteGlobalAllMessages"
]


class AdminAction(Enum):
    SetAdmin = auto()
    UnsetAdmin = auto()


@dataclass
class GroupAccess:
    set_admin: bool = False
    ban_member: bool = False
    add_member: bool = False
    change_info: bool = False
    view_admins: bool = False
    view_members: bool = False
    pin_messages: bool = False
    send_messages: bool = False
    set_join_link: bool = False
    set_member_access: bool = False
    edit_all_messages: bool = False
    delete_global_all_messages: bool = False

    def write(self) -> Union[list[str], None]:
        access_list = []

        for name, status in self.__dict__.items():
            if status:
                access = "".join([i.capitalize() for i in name.split("_")])
                access_list.append(access)

        return access_list if access_list else None

    def read(cls, data: dict[str, Any]) -> "GroupAccess":
        return cls(
            ...
        )

    @classmethod
    def all(cls) -> list[str]:
        return ACCESS_LIST


class SetGroupAdmin:
    async def set_group_admin(
        self: "rubigram.Client",
        group_guid: str,
        member_guid: str,
        access_list: Optional["GroupAccess"] = None,
        action: AdminAction = AdminAction.SetAdmin,
    ):
        if isinstance(access_list, GroupAccess):
            access_list = access_list.write()

        return await self.invoke("setGroupAdmin", {
            "group_guid": group_guid,
            "member_guid": member_guid,
            "action": action,
            "access_list": access_list,
        })

    async def unset_group_admin(
        self: "rubigram.Client",
        group_guid: str,
        member_guid: str,
    ):
        return await self.set_group_admin(group_guid, member_guid, AdminAction.UnsetAdmin)  