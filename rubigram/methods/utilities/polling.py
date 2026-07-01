import time
import logging

import rubigram


logger = logging.getLogger(__name__)


def is_update_recent(update_time: int, delay: float | int = 1) -> bool:
    now = int(time.time())
    return update_time + delay >= now


class Polling:
    async def start_polling(
        self: "rubigram.Client",
        limit: int = 10,
        rate_limit: int = 1
    ):

        await self.start()
        print("Polling started...")

        try:
            while True:
                updates = await self.get_chats_updates()
                chats = updates.get("chats")
                for chat in chats:
                    time = chat["time"]
                    if is_update_recent(time, 5):
                        print(chat)
                    else:
                        print(None)
                    # print(chat["abs_object"], chat["time"], sep=": ")

        except Exception as error:
            print(error)