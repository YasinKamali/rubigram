import rubigram


class GetMessageShareUrl:
    async def get_message_url(
        self: "rubigram.Client",
        guid: str,
        message_id: str,
    ) -> ...:
        return await self.invoke('getMessageShareUrl', {
            "object_guid": guid,
            "message_id": message_id
        })