from typing import Optional, Union, Any

import rubigram
from rubigram import utils
from rubigram.enums import ParseMode


class SendMessage:
    async def send_message(
        self: "rubigram.Client",
        guid: str,
        text: str,
        reply_to_message_id: Optional[str] = None,
        metadata: Optional[Any] = None,  # Set type later,
        parse_mode: Optional["ParseMode"] = None,
        auto_delete: Optional[int] = None
    ):
        if guid.lower() in ["me", "self"]:
            guid = self.me.user_guid

        if metadata is None:
            text, metadata = self.parser.parse(text, parse_mode)

        response = await self.invoke("sendMessage", {
            "object_guid": guid,
            "text": text,
            "rnd": utils.rnd(),
            "metadata": metadata,
            "reply_to_message_id": reply_to_message_id
        })

        if auto_delete := auto_delete or self.auto_delete:
            await self.auto_delete_message(response, auto_delete)

        return response