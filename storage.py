import json

from crypto_utils import Crypto

_crypto: Crypto


def initialize_crypto(master_password):
    global _crypto
    _crypto = Crypto(master_password)


def load_passwords():
    try:
        with open("data/vault.dat", "rb") as file:
            encrypted = file.read()
            if not encrypted:
                return {}
            return json.loads(_crypto.decrypt(encrypted).decode("utf-8"))
    except FileNotFoundError:
        return {}


def save_password(dict_data):
    encrypted_data = _crypto.encrypt(json.dumps(dict_data, indent=4).encode("utf-8"))
    with open("data/vault.dat", "wb") as file:
        file.write(encrypted_data)


def search_password(search_site):
    return load_passwords().get(search_site)


def initialize_cipher(password):
    pass


def update_password():
    pass
