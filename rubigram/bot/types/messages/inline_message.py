#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from ..base import Base

# import rubigram
# from rubigram.bot.enums import ChatKeypadType, ParseMode
# from rubigram.bot.types import File, Location, AuxData, Keypad, Metadata, Message

# from typing import Optional
from dataclasses import dataclass


@dataclass()
class InlineMessage(Base):
    ...
    # sender_id: Optional[str] = None
    # text: Optional[str] = None
    # file: Optional["File"] = None
    # location: Optional["Location"] = None
    # aux_data: Optional["AuxData"] = None
    # message_id: Optional[str] = None
    # chat_id: Optional[str] = None
    # bot: Optional["rubigram.Bot"] = None

    # @classmethod
    # def read(cls, data: dict[str, any]) -> "InlineMessage":

    #     file = data.get("file")
    #     location = data.get("location")
    #     aux_data = data.get("aux_data")

    #     return cls(
    #         sender_id=data.get("sender_id"),
    #         text=data.get("text"),
    #         message_id=data.get("message_id"),
    #         chat_id=data.get("chat_id"),
    #         file=File.read(file) if file else None,
    #         location=Location.read(location) if location else None,
    #         aux_data=AuxData.read(aux_data) if aux_data else None
    #     )

    # async def reply(
    #     self,
    #     text: str,
    #     chat_keypad: Optional["Keypad"] = None,
    #     inline_keypad: Optional["Keypad"] = None,
    #     chat_keypad_type: "ChatKeypadType" = ChatKeypadType.NONE,
    #     disable_notification: bool = False,
    #     quote: bool = False,
    #     metadata: Optional["Metadata"] = None,
    #     parse_mode: Optional["ParseMode"] = None,
    #     auto_delete: Optional[int] = None
    # ) -> "Message":
    #     if self.chat_id.startswith("b0") and not quote:
    #         reply_id = None
    #     else:
    #         reply_id = self.message_id

    #     return await self.bot.send_message(
    #         self.chat_id,
    #         text,
    #         chat_keypad,
    #         inline_keypad,
    #         chat_keypad_type,
    #         disable_notification,
    #         reply_id,
    #         metadata,
    #         parse_mode,
    #         auto_delete
    #     )