# 🔐 PyPasswordManager

A secure desktop password manager built with **Python** and **Tkinter**.  
It provides a simple and user-friendly interface for securely storing website credentials using an encrypted local vault.

---

## ✨ Features

- 🔑 Master Password Authentication
- 🔒 Master password hashing with **bcrypt**
- 🛡️ Encrypted password vault using **Fernet**
- 🔐 Encryption key derived with **PBKDF2-HMAC-SHA256**
- 🎲 Secure password generator
- 🔍 Search saved credentials
- 💾 Save and overwrite website credentials
- 📋 Copy generated passwords to clipboard
- 🧩 Modular project architecture
- 💻 Local encrypted storage

---

## 🏗️ Project Structure

```text
PyPasswordManager/
│
├── auth.py              # Master password authentication
├── crypto_utils.py      # Encryption and decryption
├── generator.py         # Password generator
├── storage.py           # Vault storage operations
├── ui.py                # Tkinter user interface
├── main.py              # Application entry point
│
├── assets/
│   └── logo.png
│
└── data/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/vardhon/PyPasswordManager.git
```

Navigate to the project folder:

```bash
cd PyPasswordManager
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## 🔑 First Launch

When running the application for the first time, you'll be prompted to create a **Master Password**.

The application automatically creates:

- `data/master.key` (stores the hashed master password)
- `data/pass.json` (encrypted password vault)

These files are excluded from version control through `.gitignore` to protect sensitive data.

---

## 🔒 Security

- Master passwords are **hashed using bcrypt**.
- Password entries are **encrypted using Fernet** before being written to disk.
- Encryption keys are **derived from the master password using PBKDF2-HMAC-SHA256**.
- Passwords are **never stored in plaintext**.

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- bcrypt
- cryptography
- JSON
- pyperclip

---

## 📌 Planned Features

- ✏️ Edit saved credentials
- 🗑️ Delete saved credentials
- 👁️ Show / Hide password
- 📊 Password strength indicator
- 🔄 Change master password
- 🧂 Random salt generation
- 💾 Automatic encrypted backups
- ☁️ Cloud synchronization
- 📱 Android companion application

---

## 📄 License

This project is licensed under the **MIT License**.
