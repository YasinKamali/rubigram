import rubigram
from rubigram.crypto import Crypto
from rubigram.enums import SignInStatus
from rubigram.errors import CodeIsInvalid
from rubigram.types import SignIn as Sign
from rubigram.utils import parse_phone_number


class SignIn:
    async def sign_in(
        self: "rubigram.Client",
        phone_number: str,
        phone_code: str,
        phone_code_hash: str
    ) -> "Sign":
        public_key, self.private_key = self.crypto.create_keys()

        data = {
            "phone_code": phone_code.strip(),
            "phone_number": parse_phone_number(phone_number),
            "phone_code_hash": phone_code_hash,
            "public_key": public_key
        }

        response = await self.invoke("signIn", data, tmp_session=True) or {}
        sign = Sign.read(response)

        self.auth = sign.decode_auth
        self.crypto = Crypto(self.auth, self.private_key)

        if sign.status == SignInStatus.CODE_IS_INVALID:
            raise CodeIsInvalid(status="CODE_IS_INVALID")

        return sign