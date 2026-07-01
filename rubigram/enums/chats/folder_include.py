from enum import Enum, auto


class FolderInclude(Enum):
    Bots = auto()
    Groups = auto()
    Channels = auto()
    Contacts = auto()
    Services = auto()
    NonConatcts = auto()