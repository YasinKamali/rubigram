import logging

from secrets import choice
from json import dumps, loads
from typing import Optional, Union
from string import ascii_lowercase

import rubigram
from rubigram.crypto import Crypto
from rubigram.errors import RPCError, ERROR_MAP


logger = logging.getLogger(__name__)


class Invoke:
    async def invoke(
        self: "rubigram.Client",
        method: str,
        input: Optional[dict] = None,
        headers: Optional[dict] = None,
        proxy: Optional[str] = None,
        timeout: Optional[float] = None,
        tmp_session: bool = False
    ) -> Union[dict, None]:
        """Create the request"""

        if not self.auth:
            self.auth = "".join(choice(ascii_lowercase) for _ in range(32))

        if self.crypto is None:
            self.crypto = Crypto(self.auth)

        data_enc = self.crypto.encrypt(dumps({
            "method": method,
            "input": input,
            "client": self.client_info
        }))

        payload = {"api_version": "6", "data_enc": data_enc}

        if tmp_session:
            payload["tmp_session"] = self.auth
        else:
            payload["sign"] = self.crypto.sign(data_enc)
            payload["auth"] = self.crypto.change_auth(self.auth)

        response = await self.server.request(
            self.API_URL,
            payload=payload,
            headers=headers or self.headers,
            proxy=proxy,
            timeout=timeout
        ) or {}

        raw: dict = loads(self.crypto.decrypt(response.get("data_enc", "{}")))

        status = raw.get("status_det")

        if raw.get("status") == "OK" and "data" in raw:
            logger.debug("Success request to method: [%s]", method)
            data = raw["data"]
            data["client"] = self
            return data

        error = ERROR_MAP.get(status, RPCError)
        raise error(status)