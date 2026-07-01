from .on_message import OnMessage
from .on_start import OnStart
from .on_sotp import OnStop
from .on_connect import OnConnect
from .on_disconnect import OnDisconnect


class Decorators(
    OnMessage,
    OnStart,
    OnStop,
    OnConnect,
    OnDisconnect
):
    pass