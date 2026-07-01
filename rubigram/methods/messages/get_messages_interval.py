import rubigram


class GetMessagesInterval:
    async def get_messages_interval(
        self: "rubigram.Client",
        object_guid: str,
        middle_message_id: str,
    ) -> ...:
        return await self.invoke("getMessagesInterval", {
            "object_guid": object_guid,
            "middle_message_id": str(middle_message_id),
        })