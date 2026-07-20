from tkinter import *
from tkinter import messagebox
import storage
import generator


class PasswordManager:
    def __init__(self):
        self.search_icon = None
        self.delete_icon = None
        self.save_icon = None
        self.generate_icon = None
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
                    overwrite = messagebox.askyesno(title="Overwrite?",
                                                    message="Website already exists. Replace the stored password?")
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

    def delete_password(self):
        search_site = self.website_entry.get().strip()
        confirm = messagebox.askyesno(title="Delete?",
                                      message="Are you sure you want to delete this site?")
        if search_site:
            if confirm:
                result = storage.delete_password(search_site)
                if result:
                    messagebox.showinfo(title="Password Deleted", message="Password has been deleted")
                    self.website_entry.delete(0, END)
                    self.password_entry.delete(0, END)
                else:
                    messagebox.showinfo(title="Not found", message="No details found for this website.")
        else:
            messagebox.showinfo(title=search_site, message="Please enter a password to save it")

    def generate_password(self):
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, generator.generate_password())

    def setup_ui(self):
        self.window = Tk()
        self.window.title(string="PyPasswordManager")
        self.window.config(padx=30, pady=50)

        # icons
        self.logo = PhotoImage(file="assets/logo.png")
        self.save_icon = PhotoImage(file="assets/save_icon.png")
        self.search_icon = PhotoImage(file="assets/search_icon.png")
        self.delete_icon = PhotoImage(file="assets/delete_icon.png")
        self.generate_icon = PhotoImage(file="assets/generate_icon.png")

        # Logo
        canvas = Canvas(width=200, height=200)
        canvas.create_image(120, 100, image=self.logo)
        canvas.grid(column=2, row=1, columnspan=2)

        # Labels
        website_label = Label(text="Website:", font=("Arial", 16))
        website_label.grid(column=1, row=2, pady=(20,0))
        email_label = Label(text="Email/Username:", font=("Arial", 16))
        email_label.grid(column=1, row=3, pady=(20,0))
        password_label = Label(text="Password:", font=("Arial", 16))
        password_label.grid(column=1, row=4, pady=(20,0))

        # Entries
        self.website_entry = Entry(width=24, font="Arial", bd=1, relief="solid")
        self.website_entry.focus()
        self.website_entry.grid(column=2, row=2, ipady=3, padx=15, pady=(20,0))
        self.email_entry = Entry(width=45 ,font="Arial", bd=1, relief="solid")
        self.email_entry.insert(0, "pvara132@gmail.com")
        self.email_entry.grid(column=2, row=3, ipady=3, columnspan=3, pady=(20,0))
        self.password_entry = Entry(width=34, show="*", font="Arial", bd=1, relief="solid")
        self.password_entry.grid(column=2, row=4, ipady=3, columnspan=2, padx=(15,0), pady=(20,0))

        # Buttons
        generate_button = Button(text="Generate", image=self.generate_icon, compound="left",
                                 command=self.generate_password, bg="#757575", fg="white",
                                 activebackground="#616161", activeforeground="white", relief="flat",
                                 bd=1, cursor="hand2", font=("Arial", 13, "bold"), padx=6, pady=4)
        generate_button.grid(column=4, row=4, padx=15, pady=(20,0))

        search_button = Button(text="Search", image=self.search_icon, compound="left",
                               command=self.search_password, bg="#1976D2", fg="white", activebackground="#1565C0",
                               activeforeground="white", relief="flat", bd=1, cursor="hand2",
                               font=("Arial", 13, "bold"), padx=6, pady=4)
        search_button.grid(column=3, row=2, pady=(20,0))


        save_button = Button(text="Save Password", image=self.save_icon, compound="left",
                             command=self.add_password, bg="#4CAF50", fg="white", activebackground="#43A047",
                             activeforeground="white", relief="flat", bd=1, cursor="hand2",
                             font=("Arial", 13, "bold"), padx=6, pady=4, width=300)
        save_button.grid(column=2, row=5, columnspan=2, pady=(50,50))


        delete_button = Button(text="Delete", image=self.delete_icon, compound="left", command=self.delete_password,
                               bg="#D32F2F", fg="white", activebackground="#C62828", activeforeground="white",
                               relief="flat", bd=1, cursor="hand2", font=("Arial", 13, "bold"), padx=13, pady=4)
        delete_button.grid(column=4, row=2, pady=(20,0))

        self.window.mainloop()
