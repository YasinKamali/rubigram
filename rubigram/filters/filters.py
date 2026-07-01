import re
from typing import Optional, Pattern, Union, Any

from rubigram.types import Update
from rubigram.filters import Filter, create
from rubigram.enums import ChatType, FileType


class TextFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return bool(update.message.text)


class BotFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return update.type == ChatType.Bot


class PrivateFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return str(update.raw['chat_updates'][0]['object_guid']).startswith('u0') 
        return update.type == ChatType.User


class GroupFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return update.type == ChatType.Group


class ChannelFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return update.type == ChatType.Channel


class ServiceFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return update.type == ChatType.Service


class EditedFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return update.message.is_edited


class ForwardFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return update.message.forwarded_from is not None


class LocationFilter(Filter):
    async def __call__(self, client, update: "Update") -> bool:
        return update.message.location is not None


class CommandFilter(Filter):
    def __init__(
        self,
        command: Union[str, list[str]],
        prefix: Union[str, list[str]] = "/",
        case_sensitive: bool = False,
        startswith: bool = False
    ):
        self.command = command
        self.prefix = prefix
        self.case_sensitive = case_sensitive
        self.startswith = startswith

    async def __call__(self, client, update: "Update") -> bool:
        message = update.message
        if message.text is None:
            return False

        if isinstance(self.command, str):
            self.command = [self.command]

        if isinstance(self.prefix, str):
            self.prefix = [self.prefix]

        if not self.case_sensitive:
            commands = [c.lower() for c in self.command]

        command_list = tuple(p + c for p in self.prefix for c in commands)

        text = message.text if self.case_sensitive else message.text.lower()

        if self.startswith:
            return any(text.startswith(c) for c in command_list)
        else:
            return any(text == c for c in command_list)


class RegixFilter(Filter):
    def __init__(
        self,
        pattern: Union[str, list[str]],
        flags: int = re.IGNORECASE
    ):
        self.pattern = pattern
        self.flags = flags

    async def __call__(self, client, update: "Update"):
        text = update.message.text
        if text is None:
            return False

        if isinstance(self.pattern, str):
            self.pattern = [self.pattern]

        compiled_patterns = [re.compile(p, self.flags) for p in self.pattern]

        return any(p.search(text) for p in compiled_patterns)


class ChatFilter(Filter):
    def __init__(
        self,
        chat: Union[str, list[str]]
    ):
        self.chat = chat

    async def __call__(self, client, update: "Update"):
        if isinstance(self.chat, str):
            self.chat = [self.chat]

        return update.message.author_object_guid in self.chat


class FileFilter(Filter):
    def __init__(
        self,
        type: Optional[Union["FileType", list["FileType"]]] = None
    ):
        self.type = type

    async def __call__(self, client, update: "Update"):
        if self.type is None:
            return update.message.file_inline is not None

        if isinstance(self.type, str):
            self.type = [self.type]

        file_inline = update.message.file_inline

        return file_inline and file_inline.type in self.type


class ContactFilter(Filter):
    def __init__(
        self,
        phone_number: Optional[Union[str, list]] = None
    ):
        self.phone_number = phone_number

    async def __call__(self, client, update: "Update"):
        contact_message = update.message.contact_message

        if self.phone_number is None:
            return contact_message is not None

        if isinstance(self.phone_number, str):
            self.phone_number = [self.phone_number]

        return contact_message and contact_message.phone_number == self.phone_number


text = TextFilter()
bot = BotFilter()
private = PrivateFilter()
group = GroupFilter()
channel = ChannelFilter()
service = ServiceFilter()
edited = EditedFilter()
forward = ForwardFilter()
location = LocationFilter()


def command(
    command: Union[str, list[str]],
    prefix: Union[str, list[str]] = "/",
    case_sensitive: bool = False,
    startswith: bool = False
) -> Filter:
    return CommandFilter(command, prefix, case_sensitive, startswith)


def regix(
    pattern: Union[str, list[str]],
    flags: int = re.IGNORECASE
) -> Filter:
    return RegixFilter(pattern, flags)


def chat(
    chat: Union[str, list[str]]
) -> Filter:
    return ChatFilter(chat)


def file(
    type: Optional[Union["FileType", list["FileType"]]] = None
) -> Filter:
    return FileFilter(type)


def contact(
    phone_number: Optional[Union[str, list]] = None
) -> Filter:
    return ContactFilter(phone_number)