from .api_error import APIError


class InvalidInput(APIError):
    pass


class InvalidAccess(APIError):
    pass


class TooRequests(APIError):
    pass


class ServerError(APIError):
    pass


class RequestSendFileError(Exception):
    def __init__(self, type: str):
        self.type = type
        super().__init__(self.__str__())

    def __str__(self):
        return f"Can't get access to upload '{self.type}'"


ERROR_MAP = {
    "TOO_REQUESTS": TooRequests,
    "SERVER_ERROR": ServerError,
    "INVALID_INPUT": InvalidInput,
    "INVALID_ACCESS": InvalidAccess,
}