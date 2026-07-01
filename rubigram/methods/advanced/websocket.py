import logging
import asyncio
import aiohttp
import inspect

from typing import Any
from json import loads
from threading import Thread
from aiohttp import WSMsgType
from asyncio import create_task

import rubigram


logger = logging.getLogger(__name__)


class WebSocket:
    async def get_updates(self: "rubigram.Client"):
        create_task(self.keep_socket())

        tasks = set()

        async def dispatcher(raw_update: dict):
            data_enc = raw_update.get("data_enc")

            if not data_enc:
                return

            data: dict[str, Any] = loads(self.crypto.decrypt(data_enc))

            message_updates = data.get("message_updates", [])
            chat_updates = data.get("chat_updates", [])

            if len(message_updates) > 1:
                for i, message in enumerate(message_updates):
                    update = {
                        "message_updates": [message],
                        "chat_updates": [chat_updates[i]] if i < len(chat_updates) else [{}],
                        # "show_notifications": [notifications[i]] if i < len(notifications) else [],
                        "user_guid": data.get("user_guid"),
                        "client": self
                    }

                    try:
                        await self.dispatcher.dispatch(update)
                    except Exception as error:
                        logger.error("Error dispatching update: %s", error)

            else:
                data["client"] = self
                await self.dispatcher.dispatch(data)

        while True:
            try:
                async with self.connection.http_session.ws_connect(
                    self.WSS_URL, proxy=self.proxy
                ) as ws:
                    self.connection.ws = ws

                    await ws.send_json({
                        "method": "handShake",
                        "auth": self.auth,
                        "api_version": "6",
                        "data": ""
                    })

                    handshake_response = await ws.receive()
                    if handshake_response.type == WSMsgType.TEXT:
                        response_data = handshake_response.json()
                        if response_data.get("status") == "OK":
                            logger.info("WebSocket handshake successful")
                            if self.connect_handler:
                                await self.connect_handler.execute(self, None)
                        else:
                            logger.error(f"Handshake failed: {response_data}")
                            continue
                    else:
                        logger.error("Invalid handshake response")
                        continue

                    async for msg in ws:
                        if msg.type == WSMsgType.TEXT:
                            task = create_task(dispatcher(msg.json()))
                            tasks.add(task)
                            task.add_done_callback(tasks.discard)

                        elif msg.type in (WSMsgType.CLOSED, WSMsgType.ERROR):
                            logger.warning("WebSocket closed or errored")
                            if self.disconnect_handler:
                                await self.disconnect_handler.execute(self, None)
                            break

            except (aiohttp.ServerTimeoutError, TimeoutError, aiohttp.ClientError) as error:
                logger.warning(
                    "WebSocket connection lost: %s. Retrying in 3 seconds...", error
                )
                if self.disconnect_handler:
                    await self.disconnect_handler.execute(self, None)
                await asyncio.sleep(3)

            except Exception as error:
                logger.error(
                    f"Unexpected error in WebSocket connection: {error}", exc_info=True)
                if self.disconnect_handler:
                    await self.disconnect_handler.execute(self, None)
                await asyncio.sleep(5)

    async def keep_socket(self: "rubigram.Client") -> None:
        while True:
            if not self.connection.is_connected:
                break

            try:
                await asyncio.sleep(10)

                if self.connection.ws and not self.connection.ws.closed:
                    await self.connection.ws.send_json({})
                    await self.get_chats_updates()
                else:
                    logger.warning("WebSocket is not available for keep-alive")
                    break

            except Exception as error:
                logger.warning(
                    "Exception while keeping WebSocket alive: %s", error, exc_info=True
                )
                if self.disconnect_handler:
                    await self.disconnect_handler.execute(self, None)
                break

    async def handle_text_message(self: "rubigram.Client", message_data: dict) -> None:
        data_enc = message_data.get("data_enc")
        if not data_enc:
            logger.debug(
                "Missing 'data_enc' key in message", extra={"data": message_data}
            )
            return

        try:
            data: dict[str, Any] = loads(self.crypto.decrypt(data_enc))
            user_guid = data.pop("user_guid")

            tasks = [
                self.handle_update(
                    name, {**update, "client": self, "user_guid": user_guid}
                )
                for name, updates in data.items()
                if isinstance(updates, list)
                for update in updates
            ]

            await asyncio.gather(*tasks)

        except Exception as error:
            logger.error(
                "Exception while handling WebSocket message",
                extra={"data": message_data},
                exc_info=True,
            )

    async def handle_update(
        self: "rubigram.Client",
        name: str,
        update: dict
    ) -> None:
        tasks = []
        for func, handler in self.dispatcher.handlers.items():
            try:
                if isinstance(handler, type):
                    handler = handler()

                if not await handler(update=update):
                    continue

                update_object = update.copy()

                if not inspect.iscoroutinefunction(func):
                    if self.sequential_handlers:
                        tasks.append(asyncio.to_thread(func, update_object))
                    else:
                        Thread(target=func, args=(update_object,)).start()
                else:
                    if self.sequential_handlers:
                        tasks.append(func(update_object))
                    else:
                        create_task(func(update_object))

            except Exception as error:
                logger.error(
                    f"Error in handler for '{name}': {error}", exc_info=True)

        if tasks and self.sequential_handlers:
            await asyncio.gather(*tasks)

    # async def handle_update(
    #     self: "rubigram.Client",
    #     name: str,
    #     update: dict
    # ) -> None:

    #     for func, handler in self.dispatcher.handlers.items():
    #         try:
    #             if isinstance(handler, type):
    #                 handler = handler()

    #             if not await handler(update=update):
    #                 continue

    #             update_object = update.copy()
    #             handler_executed: bool = False

    #             if not inspect.iscoroutinefunction(func):
    #                 if self.sequential_handlers:
    #                     await asyncio.to_thread(func, update_object)
    #                 else:
    #                     Thread(target=func, args=(update_object,)).start()
    #                 handler_executed = True

    #             else:
    #                 if self.sequential_handlers:
    #                     await func(update_object)
    #                 else:
    #                     create_task(func(update_object))
    #                 handler_executed = True

    #             if handler_executed and self.sequential_handlers:
    #                 break

    #         except Exception as error:
    #             logger.error(
    #                 f"Error in handler for '{name}': {error}",
    #                 extra={"data": update},
    #                 exc_info=True,
    #             )
