from .auth import Auth
from .users import Users
from .chats import Chats
from .messages import Messages
from .advanced import Advanced
from .settings import Settings
from .utilities import Utilities
from .decorators import Decorators


class Methods(
    Auth,
    Users,
    Chats,
    Messages,
    Advanced,
    Settings,
    Utilities,
    Decorators
):
    pass