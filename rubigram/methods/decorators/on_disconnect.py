from typing import Callable, Optional

import rubigram
from rubigram.handlers import DisconnectHandler


class OnDisconnect:
    def on_disconnect(self: Optional["OnDisconnect"] = None) -> Callable:
        def decorator(func: Callable) -> Callable:
            if isinstance(self, rubigram.Client):
                self.add_handler(DisconnectHandler(func))
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((DisconnectHandler(func)))

            return func

        return decorator