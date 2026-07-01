#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Callable, Optional

import rubigram
from rubigram.bot.filters import Filter
from rubigram.bot.handlers import InlineQueryHandler


class OnInlineQuery:
    def on_inline_query(
        self: "rubigram.Bot",
        filters: Optional["Filter"] = None,
        group: int = 0
    ):
        def decorator(func: Callable) -> Callable:
            self.add_handler(InlineQueryHandler(func, filters), group)

            return func

        return decorator