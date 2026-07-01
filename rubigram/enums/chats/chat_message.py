from enum import Enum, auto


class ChatMessage(Enum):
    NotMessage = auto()
    Other = auto()
    Text = auto()