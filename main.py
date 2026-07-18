from auth import AuthManager
from ui import PasswordManager


def main():
    auth = AuthManager()

    if auth.authenticate():
        app = PasswordManager()
        app.setup_ui()


if __name__ == "__main__":
    main()
