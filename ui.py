from tkinter import *
from tkinter import messagebox
import generator
import storage

class PasswordManager:
    def __init__(self):
        self.logo = None
        self.window = None
        self.website_entry = None
        self.email_entry = None
        self.password_entry = None

    def add_password(self):
        website = self.website_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        new_dict = {
            website: {"email": email,
                      "password": password
                      }
        }

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
        else:
            try:
                data_read = storage.load_passwords()
                if website in data_read:
                    overwrite = messagebox.askyesno(title="Overwrite?", message="Website already exists. Replace the stored password?")
                    if not overwrite:
                        return
                data_read.update(new_dict)
            except FileNotFoundError:
                storage.save_password(new_dict)
            else:
                storage.save_password(data_read)

            self.website_entry.focus()
            self.website_entry.delete(0, END)
            self.password_entry.delete(0, END)

    # --------------------------- SEARCH PASSWORD ------------------------------ #
    def search_password(self):
        search_site = self.website_entry.get().strip()
        if search_site:
            try:
                search_dict = storage.search_password(search_site)
                if search_dict:
                    messagebox.showinfo(title=search_site,
                                        message=f'Email: {search_dict["email"]}\nPassword: {search_dict["password"]}')
                else:
                    messagebox.showinfo(title=search_site,
                                        message=f"Information does not exist, Please enter a password to save it")
            except FileNotFoundError:
                messagebox.showinfo(title=search_site,
                                    message=f"Information does not exist, Please enter a password to save it")
        else:
            messagebox.showinfo(title=search_site, message="Please enter a password to save it")

    def generate_password(self):
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, generator.generate_password())

    def setup_ui(self):
        self.window = Tk()
        self.window.title(string="Password Manager")
        self.window.config(padx=50, pady=50)

        # Logo
        canvas = Canvas(width=200, height=200)
        self.logo = PhotoImage(file="assets/logo.png")
        canvas.create_image(120, 100, image=self.logo)
        canvas.grid(column=2, row=1)

        # Labels
        website_label = Label(text="Website:")
        website_label.grid(column=1, row=2)
        email_label = Label(text="Email/Username:")
        email_label.grid(column=1, row=3)
        password_label = Label(text="Password:")
        password_label.grid(column=1, row=4)

        # Entries
        self.website_entry = Entry(width=32)
        self.website_entry.focus()
        self.website_entry.grid(column=2, row=2, pady=5)
        self.email_entry = Entry(width=51)
        self.email_entry.insert(0, "pvara132@gmail.com")
        self.email_entry.grid(column=2, row=3, columnspan=2, pady=5)
        self.password_entry = Entry(width=32, show="*")
        self.password_entry.grid(column=2, row=4, pady=5)

        # Buttons
        generate_button = Button(text="Generate Password", width=14, command=self.generate_password)
        generate_button.grid(column=3, row=4, padx=3)
        search_button = Button(text="Search", width=14, command=self.search_password)
        search_button.grid(column=3, row=2, padx=3)
        add_button = Button(text="Add", width=43, command=self.add_password)
        add_button.grid(column=2, row=5, columnspan=2, pady=3)

        self.window.mainloop()
