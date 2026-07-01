from enum import Enum


class SignInStatus(Enum):
    OK = "OK"
    CODE_IS_USED = "CodeIsUsed"
    CODE_IS_EXPIRED = "CodeIsExpired"
    CODE_IS_INVALID = "CodeIsInvalid"