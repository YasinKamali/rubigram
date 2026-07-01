from enum import Enum, auto


class ChatAccess(Enum):
    AcceptOwner = auto()
    AddMember = auto()
    BanMember = auto()
    ChangeInfo = auto()
    DeleteGlobalAllMessages = auto()
    DeleteGlobalMyMessages = auto()
    DeleteLocalMessages = auto()
    EditAllMessages = auto()
    EditMyMessages = auto()
    PinMessages = auto()
    RemoveObject = auto()
    SendMessages = auto()
    SetAdmin = auto()
    SetJoinLink = auto()
    SetMemberAccess = auto()
    SuperAdmin = auto()
    ViewAdmins = auto()
    ViewInfo = auto()
    ViewMembers = auto()
    ViewMessages = auto()