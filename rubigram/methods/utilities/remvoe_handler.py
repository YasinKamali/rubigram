#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


import rubigram
from rubigram.handlers import (
    Handler,
    StopHandler,
    StartHandler,
    ConnectHandler,
    DisconnectHandler
)


class RemoveHandler:
    def remove_handler(
        self: "rubigram.Client",
        handler: "Handler",
        group: int = 0
    ):
        if isinstance(handler, StartHandler):
            self.start_handler = None
        elif isinstance(handler, StopHandler):
            self.stop_handler = None
        elif isinstance(handler, ConnectHandler):
            self.connect_handler = None
        elif isinstance(handler, DisconnectHandler):
            self.disconnect_handler = None
        else:
            self.dispatcher.remove_handler(handler, group)

        return handler, group