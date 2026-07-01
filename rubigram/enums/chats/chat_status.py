from enum import Enum, auto


class ChatStatus(Enum):
    Active = auto()
    NoAccess = auto()
    NotExist = auto()
    ObjRemoved = auto()
    Stopped = auto()