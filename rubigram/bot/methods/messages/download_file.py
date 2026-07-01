import os
import logging
import aiofiles

from typing import Optional, Union

import rubigram
from rubigram import utils


logger = logging.getLogger(__name__)


class DownloadFile:
    async def download_file(
        self: "rubigram.Bot",
        file_id: str,
        name: Optional[str] = None,
        directory: Optional[str] = None,
        chunk_size: int = 1024 * 1024,
        in_memory: bool = False,
        get_url: bool = False,
        timeout: Optional[float] = None
    ) -> Union[str, bytes]:
        url = await self.get_file(file_id)
        if not url:
            raise ValueError("Can't get url from %s", file_id)

        if get_url:
            return url

        try:
            data = await self.server.request(url, "GET", timeout=timeout, chunk_size=chunk_size)
            mime = utils.get_mime_from_bytes(data)
            name = name or f"rubigram.{mime}"

            if in_memory:
                return data

            if directory:
                os.makedirs(directory, exist_ok=True)
                path = os.path.join(directory, name)
            else:
                path = name

            async with aiofiles.open(path, "wb") as fp:
                await fp.write(data)

            return path

        except Exception as error:
            logger.error("Error to download file from %s: %s", url, error)