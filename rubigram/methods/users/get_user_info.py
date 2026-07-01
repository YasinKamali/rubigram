from typing import Optional

import rubigram
from rubigram.types import User


class GetUserInfo:
    async def get_user_info(
        self: "rubigram.Client",
        user_guid: Optional[str] = None
    ) -> "User":
        response = await self.invoke("getUserInfo", {"user_guid": user_guid})
        return User.read(response.get("user") or {})