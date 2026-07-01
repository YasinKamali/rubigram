from typing import Callable, Optional

import rubigram
from rubigram.handlers import ConnectHandler


class OnConnect:
    def on_connect(self: Optional["OnConnect"] = None) -> Callable:
        def decorator(func: Callable) -> Callable:
            if isinstance(self, rubigram.Client):
                self.add_handler(ConnectHandler(func))
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((ConnectHandler(func)))

            return func

        return decorator