import rubigram
from rubigram.bot.handlers import StopHandler, StartHandler, Handler


class RemvoeHandler:
    def remove_handler(
        self: "rubigram.Bot",
        handler: "Handler",
        group: int = 0
    ):
        if isinstance(handler, StartHandler):
            self.start_handler = None
        elif isinstance(handler, StopHandler):
            self.stop_handler = None
        else:
            self.dispatcher.remove_handler(handler, group)