from typing import Union, Literal

import rubigram


class AddChannel:
    async def add_channel(
        self: "rubigram.Client",
        title: str,
        description: str = None,
        member_guids: Union[str, list] = None,
        channel_type: Literal["Private", "Public"] = "Private"
    ) -> ...:

        if isinstance(member_guids, str):
            member_guids = [member_guids]

        return await self.invoke("addChannel", {
            "description": description,
            "title": title,
            "member_guids": member_guids,
            "channel_type": channel_type
        })