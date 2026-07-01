import logging
import asyncio
import inspect
import aiofiles
import io

from os import path
from time import time
from aiohttp import ClientTimeout
from typing import Optional, Callable, Union, Any

import rubigram
from rubigram import utils
from rubigram.types import RequestSendFileResult


logger = logging.getLogger(__name__)


class Upload:
    async def upload(
        self: "rubigram.Client",
        file: Union[str, bytes,io.BytesIO],
        name: Optional[str] = None,
        mime: Optional[str] = None,
        chunk_size: Optional[int] = None,
        timeout: Optional[int] = None,
        progress: Optional[Callable] = None,
        progress_args: tuple = (),
        *args, **kwargs
    ) -> "RequestSendFileResult":

        chunk_size = chunk_size or 512 * 512

        value: Optional[bytes] = None

        if isinstance(file, bytes):
            value = file

        elif utils.islink(file):
            value = await self.server.request(file, "GET", timeout=timeout, chunk_size=chunk_size)
            name = name or utils.get_file_name_from_url(file)

        elif isinstance(file, io.BytesIO):
            value = file.getvalue()
            name = name or getattr(file, 'name', None) or f"file_{int(time())}"

        elif path.exists(file):
            name = name or path.basename(file)
            async with aiofiles.open(file, "rb") as fp:
                value = await fp.read()
        else:
            raise ValueError(f"Error to found or read file: {file}")

        size = len(value)
        mime = mime or utils.get_mime_from_bytes(value)
        filename = name or f"rubigram{int(time())}.{mime}"

        # Get upload URL from RUBIKA server
        response = await self.request_send_file(filename, size, mime)
        url = response.upload_url

        if not url:
            raise ValueError(f"Can't receive upload URL form: {filename}")

        total_parts = (size + chunk_size - 1) // chunk_size
        file_id = response.id
        access_hash_send = response.access_hash_send

        index = 0
        upload_result = None

        async def call_progress(uploaded: int, total: int):
            if progress is not None:
                try:
                    if inspect.iscoroutinefunction(progress):
                        await progress(uploaded, total, *progress_args)
                    else:
                        progress(uploaded, total, *progress_args)
                except:
                    pass

        while index < total_parts:
            start = index * chunk_size
            end = min(start + chunk_size, size)
            chunk_data = value[start:end]
            part_number = index + 1

            headers = {
                "auth": self.auth,
                "file-id": file_id,
                "total-part": str(total_parts),
                "part-number": str(part_number),
                "chunk-size": str(len(chunk_data)),
                "access-hash-send": access_hash_send,
            }

            retry_count = getattr(self, 'retry', 3)
            backoff_time = getattr(self, 'backoff', 1)

            for attempt in range(1, retry_count + 1):
                try:
                    upload = await self.upload_chunk(url, chunk_data, headers, timeout)
                    status = upload.get("status")

                    if status == "ERROR_TRY_AGAIN":
                        response = await self.request_send_file(filename, size, mime)
                        url = response.upload_url
                        file_id = response.id
                        access_hash_send = response.access_hash_send
                        index = 0
                        break

                    if status == "OK":
                        upload_result = upload
                        uploaded_size = min((index + 1) * chunk_size, size)
                        await call_progress(uploaded_size, size)
                        index += 1
                        break

                    else:
                        logger.error("Error to upload: %s", upload)

                except Exception as error:
                    if attempt < retry_count:
                        await asyncio.sleep(backoff_time * (2 ** (attempt - 1)))
                    else:
                        raise Exception(
                            f"Error to upload chunk {part_number} after {retry_count} attempts: {error}"
                        )

        if upload_result and upload_result.get("status") == "OK":
            response.mime = mime
            response.name = filename
            response.size = size
            response.file = value
            response.access_hash_rec = upload_result["data"]["access_hash_rec"]
            return response

        raise Exception("Upload failed: Unable to complete upload process")

    async def upload_chunk(
        self: "rubigram.Client",
        url: str,
        data: bytes,
        headers: dict,
        timeout: Optional[int] = None
    ) -> dict[str, Any]:
        request_data = {"data": data, "headers": headers}

        if timeout:
            timeout_obj = ClientTimeout(total=timeout)
            request_data["timeout"] = timeout_obj

        async with self.connection.http_session.post(url, **request_data) as response:
            response.raise_for_status()
            return await response.json()