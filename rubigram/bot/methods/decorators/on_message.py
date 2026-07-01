#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Callable, Optional,Union

import rubigram
from rubigram.bot.filters import Filter
from rubigram.bot.handlers import MessageHandler
 

class OnMessage:
    def on_message(
        self: Optional[Union["rubigram.Bot",Filter]] = None,
        filters: Optional["Filter"] = None,
        group: int = 0
    ):
        def decorator(func: Callable) -> Callable:
            if isinstance(self, rubigram.Bot):
                self.add_handler(MessageHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
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
