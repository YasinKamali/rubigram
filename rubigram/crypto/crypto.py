import base64

from typing import Optional
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, urlsafe_b64decode
from string import ascii_lowercase, ascii_uppercase

from ... import utils


class Crypto:
    def __init__(
        self,
        auth: str,
        private_key: Optional[str] = None
    ):
        self.auth = auth
        self.key = bytearray(Crypto.secret(auth), "utf-8")
        self.iv = bytearray.fromhex("0" * 32)
        self.iv = b"\x00" * 16

        if private_key:
            private_key = utils.format_key(private_key)
            self.keypair = RSA.import_key(private_key.encode())

    @staticmethod
    def secret(e: str) -> str:
        e: str = e[16:24] + e[0:8] + e[24:32] + e[8:16]
        data: list[str] = []

        for c in e:
            if "0" <= c <= "9":
                data.append(chr((ord(c) - 48 + 5) % 10 + 48))
            else:
                data.append(chr((ord(c) - 97 + 9) % 26 + 97))

        return "".join(data)

    @staticmethod
    def change_auth(auth: str) -> str:
        data: list[str] = []
        for c in auth:
            if c.lower():
                data.append(chr((32 - (ord(c) - 97)) % 26 + 97))
            elif c.isupper():
                data.append(chr((29 - (ord(c) - 65)) % 26 + 65))
            elif c.isdigit():
                data.append(chr((13 - (ord(c) - 48)) % 10 + 48))
            else:
                data.append(c)

        return "".join(data)

    def encrypt(self, plain: str) -> str:
        raw = pad(plain.encode(), AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        return b64encode(aes.encrypt(raw)).decode()

    def decrypt(self, cipher: str) -> str:
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(urlsafe_b64decode(cipher))
        return unpad(dec, AES.block_size).decode()

    def sign(self, data: str) -> str:
        h = SHA256.new(data.encode())
        return b64encode(pkcs1_15.new(self.keypair).sign(h)).decode()

    def rsa_keygen(self):
        keypair = RSA.generate(1024)
        public_key = Crypto.change_auth(
            b64encode(keypair.publickey().export_key()).decode()
        )
        private_key = keypair.export_key().decode()
        return public_key, private_key

    @staticmethod
    def decode_auth(auth: str) -> str:
        """
        Decode an auth string by applying character substitutions.

        Args:
            auth (str): The input auth string.

        Returns:
            str: The decoded auth string.
        """
        result_list, digits = [], "0123456789"
        translation_table_lower = str.maketrans(
            ascii_lowercase,
            "".join([chr(((32 - (ord(c) - 97)) % 26) + 97)
                    for c in ascii_lowercase]),
        )
        translation_table_upper = str.maketrans(
            ascii_uppercase,
            "".join([chr(((29 - (ord(c) - 65)) % 26) + 65)
                    for c in ascii_uppercase]),
        )

        for char in auth:
            if char in ascii_lowercase:
                result_list.append(char.translate(translation_table_lower))
            elif char in ascii_uppercase:
                result_list.append(char.translate(translation_table_upper))
            elif char in digits:
                result_list.append(chr(((13 - (ord(char) - 48)) % 10) + 48))
            else:
                result_list.append(char)

        return "".join(result_list)

    @staticmethod
    def create_keys() -> tuple:
        """
        Generate RSA public and private keys.

        Returns:
            tuple: A tuple containing the base64-encoded public key and the private key.
        """
        keys = RSA.generate(1024)
        public_key = Crypto.decode_auth(
            base64.b64encode(keys.publickey().export_key()).decode("utf-8")
        )
        private_key = keys.export_key().decode("utf-8")
        return public_key, private_key

    @staticmethod
    def decrypt_RSA_OAEP(private_key: str, data: str):
        """
        Decrypt data using RSA OAEP encryption.

        Args:
            private_key (str): The RSA private key.
            data (str): The encrypted data.

        Returns:
            str: The decrypted data as a string.
        """
        key = RSA.import_key(private_key.encode("utf-8"))
        return PKCS1_OAEP.new(key).decrypt(base64.b64decode(data)).decode("utf-8")