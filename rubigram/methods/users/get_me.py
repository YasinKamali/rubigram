import rubigram
from rubigram.types import User


class GetMe:
    async def get_me(
        self: "rubigram.Client"
    ) -> "User":
        return await self.get_user_info()