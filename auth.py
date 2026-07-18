from tkinter import *
from tkinter import messagebox
import bcrypt
import os

MASTER_KEY_FILE = "data/master.key"
class AuthManager:

    def __init__(self):
        self.remaining_attempts = 3
        self.window = None
        self.password_entry = None
        self.enter_pass_entry = None
        self.re_pass_entry = None
        self.authenticated = False

    def login(self, event=None):
        if self.remaining_attempts != 0:
            password = self.password_entry.get().strip()
            if password:
                with open(MASTER_KEY_FILE, mode="r") as data:
                    stored_hash = (data.read().strip()).encode("utf-8")
                if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
                    self.window.destroy()
                    self.authenticated = password
                else:
                    self.remaining_attempts -= 1
                    self.password_entry.delete(0, END)
                    self.password_entry.focus()
                    messagebox.showinfo(message=f"Incorrect Password\nRemaining chances: {self.remaining_attempts}")
                    if self.remaining_attempts == 0:
                        self.window.destroy()
            else:
                messagebox.showinfo(message="Enter the password!")

    def signup(self, event=None):
        p1 = self.enter_pass_entry.get().strip()
        p2 = self.re_pass_entry.get().strip()
        if p1 == p2:
            if len(p1) >= 8:
                hashed_pass = (bcrypt.hashpw(p1.encode("utf-8"), bcrypt.gensalt())).decode()
                with open(MASTER_KEY_FILE, mode="w") as data:
                    data.write(hashed_pass)
                self.window.destroy()
                self.authenticated = p1
            else:
                messagebox.showinfo(message="Minimum 8 characters required!")
        else:
            messagebox.showinfo(message="Passwords do not match!")

    def create_login_window(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.config(padx=50, pady=50)

        password_label = Label(text="Password:")
        password_label.grid(column=1, row=1)
        self.password_entry = Entry(width=30, show="*")
        self.password_entry.grid(column=2, row=1)
        self.password_entry.focus()
        self.password_entry.bind("<Return>", self.login)
        search_button = Button(text="Proceed", width=33, command=self.login)
        search_button.grid(column=1, row=2, columnspan=2, pady=10)

        self.window.mainloop()

    def create_signup_window(self):
        self.window = Tk()
        self.window.title(string="Create Master Password")
        self.window.config(padx=50, pady=50)

        enter_pass_label = Label(text="‎ ‎ ‎ ‎ ‎ ‎ Enter password:")
        enter_pass_label.grid(column=1, row=1)
        self.enter_pass_entry = Entry(width=30, show="*")
        self.enter_pass_entry.focus()
        self.enter_pass_entry.bind("<Return>", lambda event: self.re_pass_entry.focus())
        self.enter_pass_entry.grid(column=2, row=1)

        re_pass_label = Label(text="Re-enter password:")
        re_pass_label.grid(column=1, row=2)
        self.re_pass_entry = Entry(width=30, show="*")
        self.re_pass_entry.grid(column=2, row=2)
        self.re_pass_entry.bind("<Return>", self.signup)

        proceed_button = Button(text="Proceed", width=41, command=self.signup)
        proceed_button.grid(column=1, row=3, columnspan=2, pady=10)

        self.window.mainloop()

    def authenticate(self):
        if os.path.exists(MASTER_KEY_FILE):
            self.create_login_window()
        else:
            self.create_signup_window()
        return self.authenticated
