#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Callable, Optional

import rubigram
from rubigram.filters import Filter
from rubigram.handlers import MessageHandler


class OnMessage:
    def on_message(
        self: "rubigram.Client",
        filters: Optional["Filter"] = None,
        group: int = 0
    ) :
        def decorator(func: Callable) -> Callable:
            if isinstance(self, rubigram.Client):
                self.add_handler(MessageHandler(func, filters), group)
            elif isinstance(self, Filter):
                if not hasattr(func, "handlers"):
                    func.handlers = []
                func.handlers.append(
                    (
                        MessageHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator
