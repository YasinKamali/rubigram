import rubigram


class DeleteChatHistory:
    async def delete_chat_history(
        self: "rubigram.Client",
        guid: str,
        last_message_id: str,
    ) -> ...:
        return await self.invoke("deleteChatHistory", {
            "object_guid": guid,
            "last_message_id": str(last_message_id),
        })