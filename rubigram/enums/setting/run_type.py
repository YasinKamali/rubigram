from enum import Enum, auto


class RunType(Enum):
    Polling = auto()
    WebSocket = auto()