#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from pathlib import Path
from typing import Optional, Union

import rubigram
from rubigram.utils import remvoe_none_value
from rubigram.bot.types import Keypad, Message, Metadata
from rubigram.bot.enums import ChatKeypadType, ParseMode, FileType


class SendFile:
    async def send_file(
        self: "rubigram.Bot",
        chat_id: str,
        file: Union[str, bytes],
        name: Optional[str] = None,
        caption: Optional[str] = None,
        type: "FileType" = FileType.FILE,
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
        url = await self.request_send_file(type)

        if isinstance(file, str) and (not file.startswith("http") and not Path(file).exists()):
            file = await self.get_file(file)

        file_id = await self.upload(url, file, name, timeout)
        if not file_id:
            raise ValueError("Can't get file_id from %s", file)

        if metadata is None:
            caption, metadata = self.parser.parse(caption, parse_mode)

        data = remvoe_none_value({
            "chat_id": chat_id,
            "file_id": file_id,
            "text": caption,
            "metadata": metadata,
            "chat_keypad": chat_keypad.write() if chat_keypad else None,
            "inline_keypad": inline_keypad.write() if inline_keypad else None,
            "chat_keypad_type": chat_keypad_type.value,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id
        })
        
        response = await self.invoke("sendFile", data, timeout)

        message = Message.read(response)
        message.bot = self
        message.chat_id = chat_id
        message.file_id = file_id

        if auto_delete := auto_delete or self.auto_delete:
            await self.auto_delete_message(message, auto_delete)

        return message