from enum import Enum


class SentCodeStatus(Enum):
    OK = "OK"
    SEND_PASS_KEY = "SendPassKey"
    INVALID_PASS_KEY = "InvalidPassKey"