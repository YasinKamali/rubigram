import logging
import asyncio

from io import BytesIO
from typing import Optional, Literal, Union
from aiohttp import ClientTimeout, FormData

from rubigram.connection import Connection


logger = logging.getLogger(__name__)


class Server:
    def __init__(
        self,
        connection: Connection,
        retry: int,
        delay: Union[int, float],
        backoff: Union[int, float],
        proxy: Optional[str] = None,
        headers: Optional[dict] = None
    ):
        self.connection = connection
        self.retry = retry
        self.delay = delay
        self.backoff = backoff
        self.proxy = proxy
        self.headers = headers

    async def request(
        self,
        url: str,
        method: Literal["GET", "POST"] = "POST",
        *,
        payload: Optional[dict] = None,
        headers: Optional[dict] = None,
        form_data: Optional[dict] = None,
        raw_data: Optional[bytes] = None,
        proxy: Optional[str] = None,
        timeout: Optional[float] = None,
        chunk_size: int = 512 * 512
    ) -> Union[dict, bytes, None]:
        """Build custom request"""

        data: dict = {
            "json": payload,
            "proxy": proxy or self.proxy,
            "headers": headers or self.headers,
        }

        if raw_data:
            data["data"] = raw_data

        if timeout:
            data["timeout"] = ClientTimeout(timeout)

        delay = self.delay
        exception: Exception = None

        for attempt in range(1, self.retry + 1):
            try:
                if isinstance(form_data, dict):
                    form = FormData()
                    form.add_field(
                        name="file",
                        value=form_data.get("value"),
                        filename=form_data.get("filename"),
                        content_type="application/octet-stream"
                    )
                    data["data"] = form
                async with self.connection.http_session.request(method, url, **data) as response:
                    response.raise_for_status()
                    if method == "POST":
                        return await response.json()

                    buffer = BytesIO()
                    async for chunk in response.content.iter_chunked(chunk_size):
                        buffer.write(chunk)

                    buffer.seek(0)
                    return buffer.getvalue()

            except Exception as error:
                logger.error(
                    "Request attempt %s/%s failed: %s",
                    attempt, self.retry, error
                )
                exception = error
                await asyncio.sleep(delay)
                delay += self.backoff

        raise exception