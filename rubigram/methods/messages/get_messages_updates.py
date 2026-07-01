from time import time

import rubigram


class GetMessagesUpdates:
    async def get_messages_updates(
        self: "rubigram.Client",
        object_guid: str,
        state: int = round(time()) - 150,
    ) -> ...:
        return await self.invoke("getMessagesUpdates", {
            "object_guid": object_guid,
            "state": int(state),
        })