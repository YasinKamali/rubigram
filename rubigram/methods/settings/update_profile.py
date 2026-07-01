from typing import Optional
import rubigram


class UpdateProfile:
    async def update_profile(
        self: "rubigram.Client",
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        bio: Optional[str] = None,
        birth_date: Optional[str] = None,
    ) -> ...:
        data = {"updated_parameters": []}

        if first_name is not None:
            data["updated_parameters"].append("first_name")
            data["first_name"] = first_name

        if last_name is not None:
            data["updated_parameters"].append("last_name")
            data["last_name"] = last_name

        if bio is not None:
            data["updated_parameters"].append("bio")
            data["bio"] = bio

        if birth_date is not None:
            data["updated_parameters"].append("birth_date")
            data["birth_date"] = birth_date

        return await self.invoke("updateProfile", data)