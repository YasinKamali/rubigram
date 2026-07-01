from typing import Optional, Union

import rubigram
from rubigram.bot.types import Keypad, Message, Metadata
from rubigram.bot.enums import ChatKeypadType, ParseMode, FileType


class SendVoice:
    async def send_voice(
        self: "rubigram.Bot",
        chat_id: str,
        voice: Union[str, bytes],
        name: Optional[str] = None,
        caption: Optional[str] = None,
        chat_keypad: Optional["Keypad"] = None,
        inline_keypad: Optional["Keypad"] = None,
        chat_keypad_type: Optional["ChatKeypadType"] = ChatKeypadType.NONE,
        metadata: Optional["Metadata"] = None,
        parse_mode: Optional["ParseMode"] = None,
        disable_notification: bool = False,
        reply_to_message_id: Optional[str] = None,
        auto_delete: Optional[int] = None,
        timeout: Optional[float] = None
    ) -> "Message":
        return await self.send_file(
            chat_id,
            voice,
            name,
            caption,
            FileType.VOICE,
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            metadata,
            parse_mode,
            disable_notification,
            reply_to_message_id,
            auto_delete,
            timeout
        )