from typing import Optional

import rubigram
from rubigram.types import User


class UpdateUsername:
    async def update_username(
        self: "rubigram.Client",
        username: str
    ) -> "User":
        response = await self.invoke("UpdateUsername", {"username": username.replace("@", "").strip()})
        return response
        # return User.read(response.get("user") or {})