from tkinter import *
from tkinter import messagebox #message box = Helps to pop up a dialog box to confirm or ask for an action
from random import randint, choice, shuffle #Helps to minimize the code len
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    #Password Generator Project
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(8,10))]
    password_numbers = [choice(numbers)for _ in range(randint(2,4))]
    password_symbols = [choice(symbols)for _ in range(randint(2,4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS!", message="Fill the empty fields")

    else:
        is_ok = messagebox.askokcancel(title="Alert!", message= f"Do you want to save: \n webiste : {website}"
                                                f"\n email: {email}" f"\n passowrd: {password}")
        if is_ok:
            with open("passwords_data.txt", "a") as data_file:
                data_file.write(f"website: {website} | email: {email} | pwd: {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

#canvas
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image= logo)
canvas.grid(row=0, column=1)

#lables:
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
mail_entry = Entry(width=52)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "devopsmails1@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

#Buttons:
pw_generate_button = Button(text= "Generate Password", width=15, command=password_generator)
pw_generate_button.grid(row=3, column=2)
add_button = Button(text= "Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()
