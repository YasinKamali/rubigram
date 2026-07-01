from typing import Optional

import rubigram
from rubigram.types import SentCode
from rubigram.utils import parse_phone_number
from rubigram.enums import SentCodeType, SentCodeStatus
from rubigram.errors import SendPassword, InvalidPassword


class SendCode:
    async def send_code(
        self: "rubigram.Client",
        phone_number: Optional[str] = None,
        password: Optional[str] = None,
        type: "SentCodeType" = SentCodeType.SMS
    ) -> "SentCode":
        
        data = {
            "phone_number": parse_phone_number(phone_number),
            "pass_key": password,
            "send_type": type.value
        }

        response = await self.invoke("sendCode", data, self.headers, tmp_session=True)
        sent_code = SentCode.read(response, phone_number=phone_number)

        if sent_code.status == SentCodeStatus.SEND_PASS_KEY:
            raise SendPassword(status="SEND_PASSWORD")

        if sent_code.status == SentCodeStatus.INVALID_PASS_KEY:
            raise InvalidPassword(status="INVALID_PASSWORD")

        return sent_code