from typing import Union

import rubigram


class GetMessagesByID:
    async def get_messages_by_id(
        self: "rubigram.Client",
        guid: str,
        message_ids: Union[str, list]
    ) -> ...:
        if isinstance(message_ids, str):
            message_ids = [str(message_ids)]

        return await self.invoke("getMessagesByID", {
            "object_guid": guid,
            "message_ids": message_ids,
        })