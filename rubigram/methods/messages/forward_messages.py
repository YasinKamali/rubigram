from typing import Union

import rubigram
from rubigram import utils


class ForwardMessages:
    async def forward_messages(
        self: "rubigram.Client",
        from_chat: str,
        to_chat: str,
        message_ids: Union[str, list[str]],
        drop_author: bool = False
    ) -> ...:
        if not isinstance(message_ids, list):
            message_ids = [str(message_ids)]

        if to_chat in ["me", "self"]:
            to_chat = self.guid

        return await self.invoke("forwardMessages", {
            "from_object_guid": from_chat,
            "to_object_guid": to_chat,
            "message_ids": message_ids,
            "drop_author": drop_author,
            "rnd": utils.rnd()
        })