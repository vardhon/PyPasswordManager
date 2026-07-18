from auth import AuthManager
from ui import PasswordManager
import storage


def main():
    auth = AuthManager()

    master_password = auth.authenticate()

    if master_password:
        storage.initialize_crypto(master_password)
        app = PasswordManager()
        app.setup_ui()


if __name__ == "__main__":
    main()
