from typing import Literal, Union

import rubigram


class DeleteMessages:
    async def delete_messages(
        self: "rubigram.Client",
        object_guid: str,
        message_ids: Union[str, list],
        type: Literal["Local", "Global"] = "Global",
    ) -> ...:

        if isinstance(message_ids, str):
            message_ids = [message_ids]

        return await self.invoke("deleteMessages", {
            "object_guid": object_guid,
            "message_ids": message_ids,
            "type": type,
        })