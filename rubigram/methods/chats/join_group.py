import rubigram


class JoinGroup:
    async def join_group(
        self: "rubigram.Client",
        link: str,
    ) -> ...:
        if '/' in link:
            link = link.split('/')[-1]

        return await self.invoke("joinGroup", {"hash_link": link})