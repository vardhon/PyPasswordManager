import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def _make_key(password):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b'static_salt_1234', iterations=100_000)
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


class Crypto:
    def __init__(self, password):
        self.key = _make_key(password)
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data)

    def decrypt(self, data):
        return self.cipher.decrypt(data)
