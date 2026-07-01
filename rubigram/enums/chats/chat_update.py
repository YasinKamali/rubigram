from enum import Enum, auto


class ChatUpdate(Enum):
    New = auto()
    Edit = auto()
    Delete = auto()