from .invoke import Invoke
from .websocket import WebSocket
from .upload import Upload
from .request_send_file import RequestSendFile


class Advanced(
    Invoke,
    WebSocket,
    Upload,
    RequestSendFile
):
    pass