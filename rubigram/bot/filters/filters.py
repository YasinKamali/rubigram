#  Rubigrambot - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import re
from typing import Callable, Optional, Union

import rubigram
from rubigram.bot.types import Update, InlineMessage


CUSTOM_FILTER_NAME = "CustomFilter"
URL_PATTERN = re.compile(
    r"(?:(?:https?|ftp):\/\/)?(?:www\.)?[a-z0-9]+(?:[.\-][a-z0-9]+)*\.[a-z]{2,}(?:\/[^\s]*)?",
    re.IGNORECASE
)
USERNAME_PATTERN = re.compile(r"@[A-Za-z0-9_]{3,32}")


class Filter:
    def __init__(self, func):
        self.func = func

    async def __call__(self, bot, update):
        return await self.func(bot, update)

    def __and__(self, other):
        async def func(bot, update):
            return await self(bot, update) and await other(bot, update)
        return Filter(func)

    def __or__(self, other):
        async def func(bot, update):
            return await self(bot, update) or await other(bot, update)
        return Filter(func)

    def __invert__(self):
        async def func(bot, update):
            return not await self(bot, update)
        return Filter(func)


def create(func: Callable, name: Optional[str] = None, **kwargs) -> Filter:
    return type(
        name or func.__name__ or CUSTOM_FILTER_NAME,
        (Filter,),
        {"__call__": func, **kwargs}
    )()


async def gif_filter(bot, update: "Update") -> bool:
    message = update.new_message
    if not message:
        return False
    file = message.file
    if not file:
        return False
    return bool(file.size and file.size < 1024 * 1024)


async def caption_filter(bot, update: "Update") -> bool:
    message = update.new_message
    if not message:
        return False
    file = message.file
    return bool(file and update.new_message.text)


async def reply_filter(bot, update: "Update") -> bool:
    message = update.new_message
    return bool(message and getattr(message, "reply_to_message_id", None))


async def text_filter(bot, update: "Update") -> bool:
    return bool(getattr(update, "text", None))


async def file_filter(bot, update: "Update") -> bool:
    message = update.new_message
    return bool(message and getattr(message, "file", None))


async def live_filter(bot, update: "Update") -> bool:
    message = update.new_message
    return bool(message and getattr(message, "live_location", None))


async def poll_filter(bot, update: "Update") -> bool:
    message = update.new_message
    return bool(message and getattr(message, "poll", None))


async def contact_filter(bot, update: "Update") -> bool:
    message = update.new_message
    return bool(message and getattr(message, "contact_message", None))


async def sticker_filter(bot, update: "Update") -> bool:
    message = update.new_message
    return bool(message and getattr(message, "sticker", None))


async def location_filter(bot, update: "Update") -> bool:
    message = update.new_message
    return bool(message and getattr(message, "location", None))


async def forward_filter(bot, update: "Update") -> bool:
    message = update.new_message
    return bool(message and getattr(message, "forwarded_from", None))


async def edited_filter(bot, update: "Update") -> bool:
    return bool(update.updated_message)


async def group_filter(bot, update: Union["Update", "InlineMessage"]) -> bool:
    return update.chat_id.startswith("g0")


async def channel_filter(bot, update: Union["Update", "InlineMessage"]) -> bool:
    return update.chat_id.startswith("c0")


async def private_filter(bot, update: Union["Update", "InlineMessage"]) -> bool:
    return update.chat_id.startswith("b0")


def file_type_filter(type: str):
    async def wrapper(bot, update: Update):
        message = update.new_message
        file = message.file or None
        return bool(file and file.file_type == type)
    return Filter(wrapper)


def forwarded_filter(type: str):
    async def wrapper(bot, update: Update):
        message = update.new_message
        forwarded = message.forwarded_from or None
        return bool(forwarded and forwarded.type_from == type)
    return Filter(wrapper)


async def url_filter(bot, update: Update) -> bool:
    text = update.text or ""
    if not text:
        return False
    return bool(URL_PATTERN.search(text))


async def hyperlink_filter(bot, update: Update):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "Link":
            return True
    return False


async def mention_filter(bot, update: Update):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "MentionText":
            return True
    return False


async def text_bold_filter(bot, update: "Update"):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "Bold":
            return True
    return False


async def text_mono_filter(bot, update: "Update"):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "Mono":
            return True
    return False


async def text_quote_filter(bot, update: "Update"):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "Quote":
            return True
    return False


async def text_italic_filter(bot, update: "Update"):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "Italic":
            return True
    return False


async def text_strike_filter(bot, update: "Update"):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "Strike":
            return True
    return False


async def text_spoiler_filter(bot, update: "Update"):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "Spoiler":
            return True
    return False


async def text_underline_filter(bot, update: "Update"):
    message = update.new_message or update.updated_message
    if not message:
        return False
    metadata = message.metadata
    if not metadata:
        return False
    for i in metadata.meta_data_parts:
        if i.type == "Underline":
            return True
    return False


async def metadata_filter(bot, update: "Update"):
    message = update.new_message or update.updated_message
    return bool(message and message.metadata)


async def username_filter(bot, update: "Update"):
    return bool(USERNAME_PATTERN.search(update.text or ""))


# Pre-defined filter instances for common use cases
username = Filter(username_filter)

metadata = Filter(metadata_filter)

text_bold = Filter(text_bold_filter)

text_mono = Filter(text_mono_filter)

text_quote = Filter(text_quote_filter)

text_italic = Filter(text_italic_filter)

text_strike = Filter(text_strike_filter)

text_spoiler = Filter(text_spoiler_filter)

text_underline = Filter(text_underline_filter)

caption = Filter(caption_filter)

reply = Filter(reply_filter)

url = Filter(url_filter)
"""Filter for messages containing URLs in text."""

hyperlink = Filter(hyperlink_filter)
"""Filter for messages with clickable hyperlinks."""

mention = Filter(mention_filter)
"""Filter for messages containing user mentions."""

text = Filter(text_filter)
"""Filter for text messages."""

file = Filter(file_filter)
"""Filter for file messages."""

live = Filter(live_filter)
"""Filter for live location messages."""

poll = Filter(poll_filter)
"""Filter for poll messages."""

contact = Filter(contact_filter)
"""Filter for contact messages."""

sticker = Filter(sticker_filter)
"""Filter for sticker messages."""

location = Filter(location_filter)
"""Filter for location messages."""

forward = Filter(forward_filter)
"""Filter for forwarded messages."""

edited = Filter(edited_filter)
"""Filter for edited messages."""

group = Filter(group_filter)
"""Filter for group chats."""

channel = Filter(channel_filter)
"""Filter for channel chats."""

private = Filter(private_filter)
"""Filter for private chats."""

gif = Filter(gif_filter)
"""Filter for GIF file messages."""

photo = file_type_filter("Image")
"""Filter for image file messages."""

video = file_type_filter("Video")
"""Filter for video file messages."""

music = file_type_filter("Music")
"""Filter for music/audio file messages."""

voice = file_type_filter("Voice")
"""Filter for voice message files."""

document = file_type_filter("File")
"""Filter for document file messages."""

forwarded_bot = forwarded_filter("Bot")
"""Filter for messages forwarded from bots."""

forwarded_user = forwarded_filter("User")
"""Filter for messages forwarded from users."""

forwarded_channel = forwarded_filter("Channel")
"""Filter for messages forwarded from channels."""


def command(
    command: Union[str, list[str]],
    prefix:  Union[str, list[str]] = "/",
    case_sensitive: bool = False,
    start_with: bool = False
) -> bool:
    commands = command if isinstance(command, list) else [command]
    prefixs = prefix if isinstance(prefix, list) else [prefix]

    if not case_sensitive:
        commands = [c.lower() for c in commands]

    command_list = tuple(p + c for p in prefixs for c in commands)

    async def wrapper(bot, update: Update):
        if update.text is None:
            return False

        text = update.text if case_sensitive else update.text.lower()
        return any(text.startswith(c) if start_with else text == c for c in command_list)

    return Filter(wrapper)


def chat(chat_id: Union[str, list[str]]) -> bool:
    async def wrapper(bot, update: Union["Update", "InlineMessage"]):
        chat_ids = chat_id if isinstance(chat_id, list) else [chat_id]
        return update.chat_id in chat_ids
    return Filter(wrapper)


def regex(
    pattern: Union[str, list[str]],
    flags: int = re.IGNORECASE
) -> bool:
    patterns = pattern if isinstance(pattern, list) else [pattern]
    compiled_patterns = [re.compile(p, flags) for p in patterns]

    async def wrapper(bot, update: Union["Update", "InlineMessage"]):
        text = getattr(update, "text", None)
        if not text:
            return False
        return any(p.search(text) for p in compiled_patterns)

    return Filter(wrapper)


def button(
    button_id: Union[str, list[str]],
    prefix: Union[str, list[str]] = "",
    case_sensitive: bool = False
) -> bool:
    button_ids = button_id if isinstance(button_id, list) else [button_id]
    prefixs = prefix if isinstance(prefix, list) else [prefix]

    if not case_sensitive:
        button_ids = [b.lower() for b in button_ids]

    button_id_list = tuple(p + b for p in prefixs for b in button_ids)

    async def wrapper(bot, update: "InlineMessage"):
        btn_id = update.aux_data.button_id if case_sensitive else update.aux_data.button_id.lower()
        return any(btn_id.startswith(b) for b in button_id_list)
    return Filter(wrapper)


def state(
    state: Union[str, list[str]]
) -> bool:
    states = state if isinstance(state, list) else [state]

    async def wrapper(bot: "rubigram.Bot", update: Union["Update", "InlineMessage"]):
        return bot.storage.get_state(update.chat_id) in states

    return Filter(wrapper)


def sender_id(sender_id: Union[str, list[str]]) -> bool:
    sender_ids = sender_id if isinstance(sender_id, list) else [sender_id]

    async def wrapper(bot, update: "Update"):
        message = update.new_message or update.updated_message
        return bool(message and message.sender_id in sender_ids)
    return Filter(wrapper)
