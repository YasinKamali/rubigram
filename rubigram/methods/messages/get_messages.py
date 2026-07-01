from typing import Optional, Literal

import rubigram


class GetMessages:
    async def get_messages(
        self: "rubigram.Client",
        guid: str,
        max_message_id: Optional[str] = None,
        limit: int = 25,
        sort: Literal["FromMin", "FromMax"] = "FromMax",
        filter_type: Optional[str] = None
    ):
        current_max_id = max_message_id
        counter = 0

        while counter < limit:
            data = {
                "object_guid": guid,
                "sort": sort,
                "max_id": current_max_id,
                "limit": 25
            }

            if filter_type:
                data["filter_type"] = filter_type

            response = await self.invoke("getMessages", data)

            if not response or not response.get("messages"):
                break

            for message in response["messages"]:
                if counter >= limit:
                    break
                yield message
                counter += 1

            if counter >= limit:
                break

            if not response.get("has_continue"):
                break

            if response.get("new_max_id"):
                current_max_id = str(response["new_max_id"])
            else:
                current_max_id = response["messages"][-1]["message_id"]