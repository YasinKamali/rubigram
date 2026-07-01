#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import logging

from typing import Optional
from aiohttp import ClientSession, TCPConnector, ClientTimeout, ClientWebSocketResponse


logger = logging.getLogger(__name__)


class Connection:
    def __init__(
        self,
        timeout: int = 20,
        connect_timeout: int = 20,
        max_connections: int = 100,
        socket_read_timeout: int = 20,
    ):
        self.timeout = timeout
        self.connect_timeout = connect_timeout
        self.max_connections = max_connections
        self.socket_read_timeout = socket_read_timeout
        self.ws: Optional[ClientWebSocketResponse] = None

        self.client_timeout = ClientTimeout(
            timeout,
            connect_timeout,
            socket_read_timeout,
        )

        self.http_session: Optional[ClientSession] = None

    async def connect(self) -> None:
        if not self.is_connected:
            connector = TCPConnector(
                limit=self.max_connections,
                enable_cleanup_closed=True
            )

            self.http_session = ClientSession(
                connector=connector,
                timeout=self.client_timeout
            )

            logger.info(
                "Connect to HTTP session, timeout=%s, max_connections=%s",
                int(self.timeout), self.max_connections
            )

        else:
            logger.info("HTTP session already connected")

    async def disconnect(self) -> None:
        if self.is_connected and self.http_session:
            await self.http_session.close()
            logger.info("HTTP session disconnected")
        self.http_session = None

    @property
    def is_connected(self) -> bool:
        return self.http_session is not None and not self.http_session.closed

    def get_session(self) -> ClientSession:
        if not self.is_connected or not self.http_session:
            raise RuntimeError("HTTP session is not connected")
        return self.http_session

    async def __aenter__(self) -> "Connection":
        await self.connect()
        return self

    async def __aexit__(self, *args) -> None:
        await self.disconnect()