# #  RubigramClient - Rubika API library for python
# #  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
# #  Github - https://github.com/DevJavad/rubigram


import inspect
from typing import Callable, Optional

# import rubigram
# from rubigram.types import Update
from rubigram.filters import Filter


# class Handler:
#     def __init__(self, callback: Callable, filters: Optional["Filter"] = None):
#         self.callback = callback
#         self.filters = filters

#     async def execute(self, client: "rubigram.Client", update: Optional[Update] = None):
#         if self.filters is None:
#             await self.callback(client, update)
#             return True

#         if callable(self.filters):
#             if inspect.iscoroutinefunction(self.filters.__call__):
#                 result = await self.filters(client, update)
#             else:
#                 result = self.filters(client, update)

#             if result:
#                 await self.callback(client, update)
#                 return True

#             return False


import asyncio
import inspect
from typing import Optional

import rubigram
from rubigram.types import Update


class Handler:
    def __init__(self, callback: Callable, filters: Optional["Filter"] = None):
        self.callback = callback
        self.filters = filters

    async def check(self, client: "rubigram.Client", update: Update):
        if inspect.iscoroutinefunction(self.filters.__call__):
            return await self.filters(client, update)
        else:
            return await client.loop.run_in_executor(
                client.executor,
                self.filters,
                client, update
            )

    async def execute(self, client: "rubigram.Client", update: Optional[Update] = None):
        if self.filters is None or await self.check(client, update):
            if inspect.iscoroutinefunction(self.callback):
                return await self.callback(client, update)
            else:
                return await asyncio.to_thread(self.callback, client, update)

    # async def execute(self, client: "rubigram.Client", update: Optional[Update] = None):

    #     if self.filters is None:
    #         if inspect.iscoroutinefunction(self.callback):
    #             await self.callback(client, update)
    #         else:
    #             await asyncio.to_thread(self.callback, client, update)
    #         return True

    #     if callable(self.filters):
    #         if inspect.iscoroutinefunction(self.filters):
    #             result = await self.filters(client, update)
    #         else:
    #             result = await asyncio.to_thread(self.filters, client, update)

    #         if result:
    #             if inspect.iscoroutinefunction(self.callback):
    #                 await self.callback(client, update)
    #             else:
    #                 await asyncio.to_thread(self.callback, client, update)
    #             return True

    #         return False

    #     return False