#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import asyncio
from typing import Union

import rubigram


class DeleteMessage:
    async def delete_messages(
        self: "rubigram.Bot",
        chat_id: str,
        message_id: Union[str, list[str]]
    ) -> dict:
        if isinstance(message_id, str):
            return await self.invoke("deleteMessage", {"chat_id": chat_id, "message_id": message_id})

        tasks = [
            self.invoke("deleteMessage", {"chat_id": chat_id, "message_id": id}) for id in message_id
        ]

        responses = await asyncio.gather(*tasks)
        success = sum(1 for r in responses if not isinstance(r, Exception))
        failed = len(responses) - success

        return {
            "success": success,
            "failed": failed,
            "details": responses
        }