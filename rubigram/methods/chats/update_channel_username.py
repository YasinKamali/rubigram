import rubigram


class UpdateChannelUsername:
    async def update_channel_username(
        self: "rubigram.Client",
        channel_guid: str,
        username: str,
    ) -> ...:
        
        return await self.invoke("updateChannelUsername", {
            "channel_guid": channel_guid,
            "username": username.replace("@", "")
        })