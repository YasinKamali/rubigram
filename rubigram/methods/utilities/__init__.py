from .run import Run
from .stop import Stop
from .start import Start
from .get_updates import GetUpdates
from .add_handler import AddHandler
from .remvoe_handler import RemoveHandler
from .polling import Polling
from .connect import Connect
from .dsiconnect import Disconnect


class Utilities(
    Run,
    Stop,
    Start,
    GetUpdates,
    AddHandler,
    RemoveHandler,
    Polling,
    Connect,
    Disconnect
):
    pass