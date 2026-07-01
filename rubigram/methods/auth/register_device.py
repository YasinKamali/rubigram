from random import choices
from typing import Optional

import rubigram
from rubigram.enums import Platform


class RegisterDevice:
    async def register_device(
        self: "rubigram.Client",
        device_model: Optional[str] = None
    ) -> ...:
        
        data = {
            "app_version": "MA_3.4.3" if self.platform == Platform.ANDROID else "WB_4.4.27",
            "device_hash": "".join(choices("0123456789", k=26)),
            "device_model": device_model or self.device_model,
            "lang_code": "fa",
            "system_version": "SDK 28" if self.platform == Platform.ANDROID else "Windows 10",
            "token": "",
            "token_type": "Firebase" if self.platform == Platform.ANDROID else "Web"
        }

        return await self.invoke("registerDevice", data)