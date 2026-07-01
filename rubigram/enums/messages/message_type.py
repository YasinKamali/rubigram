from enum import Enum


class MessageType(Enum):
    GIF = "Gif"
    TEXT = "Text"
    LIVE = "Live"
    FILE = "File"
    IMAGE = "Image"
    VIDEO = "Video"
    MUSIC = "Music"
    VOCIE = "Voice"
    OTHER = "Other"
    EVENT = "Event"
    STICKER = "Sticker"
    FILE_INLINE = "FileInline"
    NOT_MESSAGE = "NotMessage"