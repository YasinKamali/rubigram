#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import logging
from typing import Optional, Union

import rubigram
from rubigram.bot import errors


logger = logging.getLogger(__name__)


class Invoke:
    async def invoke(
        self: "rubigram.Bot",
        method: str,
        payload: dict = {},
        timeout: Optional[int] = None,
    ) -> Union[dict, None]:

        response = await self.server.request(self.API_URL + method, payload=payload, timeout=timeout)

        status = response.get("status")

        if status == "OK" and "data" in response:
            logger.debug("Success request for (%s)", method)
            data = response.get("data")
            if "bot" in data:
                bot_info = data.pop("bot")
                data["bot_info"] = bot_info
            data["bot"] = self
            return data

        error = errors.ERROR_MAP.get(status, errors.APIError)
        raise error(response)