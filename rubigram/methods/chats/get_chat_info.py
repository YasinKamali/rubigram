import rubigram
from rubigram import utils


class GetChatInfo:
    async def get_chat_info(
        self: "rubigram.Client",
        guid: str
    ):
        chat_type = utils.get_chat_type_by_guid(guid)

        return await self.invoke(f"get{chat_type}Info", {
            f"{chat_type.lower()}_guid": guid
        })