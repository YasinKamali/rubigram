from typing import Union


class APIError(Exception):
    def __init__(self, data: dict):
        self.status: str = data.get("status")
        self.message: Union[str, None] = data.get("dev_message")

        super().__init__(self.__str__())

    def __str__(self):
        return f"status={self.status}, message={self.message}"