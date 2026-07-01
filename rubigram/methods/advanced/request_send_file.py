from typing import Optional

import rubigram
from rubigram.types import RequestSendFileResult


class RequestSendFile:
    async def request_send_file(
        self: "rubigram.Client",
        file_name: str,
        size: int,
        mime: Optional[str] = None
    ) -> "RequestSendFileResult":

        response = await self.invoke("requestSendFile", {
            "file_name": file_name,
            "size": size,
            "mime": mime or file_name.split(".")[-1]
        }) or {}

        return RequestSendFileResult.read(response)