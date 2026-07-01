#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Callable, Optional

from rubigram.bot.filters import Filter
from rubigram.bot.handlers import Handler


class InlineQueryHandler(Handler):
    def __init__(self, callback: Callable, filters: Optional["Filter"] = None):
        super().__init__(callback, filters)