# 🔐 Password Manager

A secure desktop Password Manager built with Python and Tkinter.

## Features

- Master Password Authentication
- bcrypt Password Hashing
- Password Generator
- Password Search
- Save Website Credentials
- Overwrite Existing Credentials
- Modular Architecture
- Local JSON Storage

---

## Project Structure

```
password-manager/
│
├── auth.py          # Authentication system
├── ui.py            # Main GUI
├── storage.py       # Password storage
├── generator.py     # Password generator
├── main.py          # Application entry point
│
├── assets/
│   └── logo.png
│
└── data/
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/vardhon/password-manager.git
```

Move into the project.

```bash
cd password-manager
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python main.py
```

---

## First Launch

On the first launch, you'll be asked to create a Master Password.

The application automatically creates:

- `data/master.key`
- `data/pass.json`

These files are ignored by Git for security.

---

## Technologies Used

- Python 3
- Tkinter
- bcrypt
- JSON
- pyperclip

---

## Future Improvements

- Encrypted Password Vault
- Show / Hide Password
- Password Strength Meter
- Edit Passwords
- Delete Passwords
- Automatic Backup
- Cloud Synchronization
- Android Version

---

## License

MIT License