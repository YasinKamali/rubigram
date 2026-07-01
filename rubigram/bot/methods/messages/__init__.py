#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from .auto_delete_message import AutoDeleteMessage
from .delete_messages import DeleteMessage
from .edit_chat_keypad import EditChatKeypad
from .edit_message_keypad import EditMessageKeypad
from .edit_message_text import EditMessageText
from .edit_message import EditMessage
from .forward_message import ForwardMessage
from .remove_chat_keypad import RemoveChatKeypad
from .send_contact import SendContact
from .send_file import SendFile
from .send_location import SendLocation
from .send_message import SendMessage
from .send_poll import SendPoll
from .send_sticker import SendSticker
from .send_gif import SendGif
from .send_music import SendMusic
from .send_photo import SendPhoto
from .send_video import SendVideo
from .send_voice import SendVoice
from .download_file import DownloadFile
from .request_send_file import RequestSendFile
from .upload import Upload
from .get_file import GetFile


class Messages(
    AutoDeleteMessage,
    DeleteMessage,
    EditChatKeypad,
    EditMessageKeypad,
    EditMessageText,
    EditMessage,
    ForwardMessage,
    RemoveChatKeypad,
    SendContact,
    SendFile,
    SendLocation,
    SendMessage,
    SendPoll,
    SendSticker,
    SendGif,
    SendMusic,
    SendPhoto,
    SendVideo,
    SendVoice,
    DownloadFile,
    Upload,
    RequestSendFile,

    GetFile
):
    pass