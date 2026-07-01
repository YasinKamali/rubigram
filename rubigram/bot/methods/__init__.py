#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from .decorators import Decorators
from .utilities import Utilities
from .messages import Messages
from .settings import Settings
from .advanced import Advanced
from .updates import Updates
from .chat import Chat
from .user import User


class Methods(
    Decorators,
    Utilities,
    Messages,
    Settings,
    Advanced,
    Updates,
    Chat,
    User
):
    pass