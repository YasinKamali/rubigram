#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import os
import logging
import aiofiles

from pathlib import Path
from typing import Optional, Union

import rubigram
from rubigram import utils
from rubigram.bot import errors


logger = logging.getLogger(__name__)


class Upload:
    async def upload(
        self: "rubigram.Bot",
        url: str,
        file: Union[str, bytes],
        name: Optional[str] = None,
        timeout: Optional[int] = None,
        chunk_size: int = 1024 * 1024
    ) -> Union[str, None]:
        if isinstance(file, bytes):
            data = file
            mime = utils.get_mime_from_bytes(data)
            name = name or f"rubigram.{mime}"

        elif utils.islink(file):
            data = await self.server.request(file, "GET", timeout=timeout, chunk_size=chunk_size)
            name = name or utils.get_file_name_from_url(file)

        elif os.path.exists():
            paht = Path(file)
            data = paht.read_bytes()
            name = name or paht.name

        else:
            raise ValueError(
                f"The type of file must be (path, url, bytes), your type is: {type(file)}"
            )

        response = await self.server.request(url, form_data={"value": data, "filename": name}, timeout=timeout, chunk_size=chunk_size)
        status = response.get("status")

        if status == "OK" and "data" in response:
            logger.debug("Success request for (%s)", url)
            return response["data"]["file_id"]

        error = errors.ERROR_MAP.get(status, errors.APIError)
        raise error(response)