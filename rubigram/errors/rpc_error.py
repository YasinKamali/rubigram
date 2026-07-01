from typing import Optional


class RPCError(Exception):
    def __init__(
        self,
        status: str,
        message: Optional[str] = None
    ):
        self.status = status
        self.message = message

    def __str__(self):
        return f"status={self.status}, message={self.message}"