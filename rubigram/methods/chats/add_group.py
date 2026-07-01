from typing import Optional, Union

import rubigram


class AddGroup:
    async def add_group(
        self: "rubigram.Client",
        title: str,
        member_guids: Union[str, list[str]],
        description: Optional[str] = None,
    ) -> ...:
        
        if isinstance(member_guids, str):
            member_guids = [member_guids]

        return await self.invoke("addGroup", {
            "title": title,
            "member_guids": member_guids,
            "description": description,
        })