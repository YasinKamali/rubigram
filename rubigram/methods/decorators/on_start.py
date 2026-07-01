from typing import Callable

import rubigram


class OnStart:
    def on_start(self: "rubigram.Client"):
        def decorator(func: Callable) -> Callable:
            self.add_handler(rubigram.handlers.StartHandler(func))

            return func

        return decorator