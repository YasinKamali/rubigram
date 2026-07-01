#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram
from rubigram.bot.enums import FileType
from rubigram.bot.errors import RequestSendFileError


class RequestSendFile:
    async def request_send_file(
        self: "rubigram.Bot",
        type: "FileType" = FileType.FILE
    ) -> str:
        """Request sending a file.

        Parameters:
            type (`rubigram.enums.FileType`):
                - default -> `rubigram.enums.FileType.FILE`

        Returns:
            `str` OR `None`

        Example:
        .. code-block:: python
            await bot.request_send_file(type=rubigram.enums.FileType.GIF)
        """
        if not isinstance(type, FileType):
            raise ValueError("type can only be rubigram.bot.enums.FileType")

        type = type.value

        response = await self.invoke("requestSendFile", {"type": type})
        url = response.get("upload_url")

        if url is None:
            raise RequestSendFileError(type)

        return url