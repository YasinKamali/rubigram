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


class AddHandler:
    def add_handler(
        self: "rubigram.Client",
        handler: "Handler",
        group: int = 0
    ):
        if isinstance(handler, StartHandler):
            self.start_handler = handler
        elif isinstance(handler, StopHandler):
            self.stop_handler = handler
        elif isinstance(handler, ConnectHandler):
            self.connect_handler = handler
        elif isinstance(handler, DisconnectHandler):
            self.disconnect_handler = handler
        else:
            self.dispatcher.add_handler(handler, group)

        return handler, group