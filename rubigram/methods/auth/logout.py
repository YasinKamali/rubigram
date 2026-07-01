import rubigram


class Logout:
    async def logout(
        self: "rubigram.Client"
    ) -> ...:
        return await self.invoke("logout")