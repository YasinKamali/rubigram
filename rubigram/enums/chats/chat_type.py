from enum import Enum, auto


class ChatType(Enum):
    Bot = "Bot"
    User = "User"
    Group = "Group"
    Channel = "Channel"
    Service = "Service"