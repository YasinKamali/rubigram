from typing import Callable

import rubigram


class OnStop:
    def on_stop(self: "rubigram.Client"):
        def decorator(func: Callable) -> Callable:
            self.add_handler(rubigram.handlers.StopHandler(func))

            return func

        return decorator