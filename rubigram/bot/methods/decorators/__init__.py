#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from .on_stop import OnStop
from .on_start import OnStart
from .on_message import OnMessage



class Decorators(
    OnStop,
    OnStart,
    OnMessage
):
    pass