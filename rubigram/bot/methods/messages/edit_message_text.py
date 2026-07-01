#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional

import rubigram
from rubigram.bot.enums import ParseMode
from rubigram.bot.types import Metadata


class EditMessageText:
    async def edit_message_text(
        self: "rubigram.Bot",
        chat_id: str,
        message_id: str,
        text: str,
        metadata: Optional["Metadata"] = None,
        parse_mode: Optional["ParseMode"] = None
    ) -> dict:
        if metadata is None:
            text, metadata = self.parser.parse(text, parse_mode)

        return await self.invoke(
            "editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": text,
                "metadata": metadata
            }
        )