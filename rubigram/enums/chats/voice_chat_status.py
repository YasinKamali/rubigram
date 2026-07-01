from enum import Enum, auto


class VoiceChatStatus(Enum):
    OK = auto()
    OldState = auto()
    VoiceChatNotExist = auto()