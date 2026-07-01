from .rpc_error import RPCError


class InvalidAuth(RPCError):
    def __init__(self, status, message="The Auth entered is invalid!"):
        super().__init__(status, message)


class InvalidInput(RPCError):
    def __init__(self, status, message="Invalid method input!"):
        super().__init__(status, message)


class NotRegistered(RPCError):
    def __init__(self, status, message="Method input is not registered!"):
        super().__init__(status, message)


class TooRequests(RPCError):
    def __init__(self, status, message="Too many requests! Your account has been suspended."):
        super().__init__(status, message)


class ServerError(RPCError):
    def __init__(self, status, message="Error form server"):
        super().__init__(status, message)


class InvalidMethod(RPCError):
    def __init__(self, status, message="INVALID_METHOD"):
        super().__init__(status, message)


class UsernameExists(RPCError):
    def __init__(self, status, message="USERNAME_EXIST"):
        super().__init__(status, message)


class Undeliverable(RPCError):
    def __init__(self, status, message="UNDELIVERABLE"):
        super().__init__(status, message)


class CodeIsUsed(RPCError):
    def __init__(self, status, message="Code already used"):
        super().__init__(status, message)


class CodeIsExpired(RPCError):
    def __init__(self, status, message="Code expired"):
        super().__init__(status, message)


class NotSupportedApiVersion(RPCError):
    def __init__(self, status, message="NOT_SUPPORTED_API_VERSION"):
        super().__init__(status, message)


class CodeIsInvalid(RPCError):
    def __init__(self, status, message="Code is invalid"):
        super().__init__(status, message)


class SendPassword(RPCError):
    def __init__(self, status, message="Set the account password"):
        super().__init__(status, message)


class InvalidPassword(RPCError):
    def __init__(self, status, message="Entered password is inalid!"):
        super().__init__(status, message)


ERROR_MAP = {
    "INVALID_AUTH": InvalidAuth,
    "NOT_REGISTERED": NotRegistered,
    "INVALID_INPUT": InvalidInput,
    "TOO_REQUESTS": TooRequests,
    "SERVER_ERROR": ServerError,
    "INVALID_METHOD": InvalidMethod,
    "CODE_IS_USED": CodeIsUsed,
    "CODE_IS_EXPIRED": CodeIsExpired,
    "USERNAME_EXIST": UsernameExists,
    "UNDELIVERABLE": Undeliverable,
    "NOT_SUPPORTED_API_VERSION": NotSupportedApiVersion
}