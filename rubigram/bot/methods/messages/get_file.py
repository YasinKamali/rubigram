#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Union

import rubigram


class GetFile:
    async def get_file(
        self: "rubigram.Bot",
        file_id: str
    ) -> Union[str, None]:
        """Get the file url.

        Parameters:
            file_id (`str`): The unique ID of the file.

        Returns:
            `str` OR `None`

        Example:
        .. code-block:: python
            await bot.get_file(file_id="file_id")
        """
        response = await self.invoke("getFile", {"file_id": file_id})
        return response.get("download_url")