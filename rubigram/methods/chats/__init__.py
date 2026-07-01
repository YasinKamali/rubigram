from .get_chats_updates import GetChatsUpdates
from .add_channel import AddChannel
from .add_group import AddGroup
from .join_group import JoinGroup
from .leave_group import LeaveGroup
from .set_channel_admin import SetChannelAdmin
from .update_channel_username import UpdateChannelUsername
from .join_channel import JoinChannel
from .get_chats import GetChats
from .get_chat_info import GetChatInfo
from .delete_chat_history import DeleteChatHistory
from .get_join_requests import GetJoinRequests
from .action_on_join_request import ActionOnJoinRequest
from .ban_group_member import BanGroupMember
from .ban_member import BanMember
from .get_banned_group_members import GetBannedGroupMembers
from .edit_group_info import EditGroupInfo
from .get_group_link import GetGroupLink
from .set_group_admin import SetGroupAdmin
from .get_group_admin_members import GetGroupAdminMembers


class Chats(
    GetChatsUpdates,
    AddChannel,
    AddGroup,
    JoinGroup,
    LeaveGroup,
    SetChannelAdmin,
    UpdateChannelUsername,
    JoinChannel,
    GetChats,
    GetChatInfo,
    DeleteChatHistory,
    GetJoinRequests,
    ActionOnJoinRequest,
    BanGroupMember,
    BanMember,
    GetBannedGroupMembers,
    EditGroupInfo,
    GetGroupLink,
    SetGroupAdmin,
    GetGroupAdminMembers
):
    pass