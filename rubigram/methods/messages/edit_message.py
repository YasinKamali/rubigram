from typing import Optional, Union, Any

import rubigram
from rubigram import utils
from rubigram.enums import ParseMode


class EditMessage:
    async def edit_message(
        self: "rubigram.Client",
        guid: str,
        message_id: str,
        text: str,
        parse_mode: Optional["ParseMode"] = None,
        metadata: Optional[Any] = None
    ) -> ...:
        if guid.lower() in ["me", "self"]:
            guid = self.guid

        if metadata is None:
            text, metadata = self.parser.parse(text, parse_mode)

        response = await self.invoke("editMessage", {
            "object_guid": guid,
            "text": text,
            "message_id": str(message_id),
            "metadata": metadata
        })

        return response