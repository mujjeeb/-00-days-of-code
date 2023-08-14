from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_credentials():
    password_text = (password_entry.get())
    username_text = (username_entry.get())
    website_text = (website_entry.get())

    if len(password_text) == 0 or len(website_text) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all fields")


    else:
        is_ok = messagebox.askokcancel(title="Webiste Credentials", message=f"These are the details entered \n"
                                                                            f"Email: {username_text}\n"
                                                                            f"Password: {password_text}\n"
                                                                            f"for this website: {website_text}\n is it okay to save?")

        if not is_ok:
            pass
        else:
            website_credentials = f" \n{website_text} | {username_text} | {password_text}"
            f = open("data.txt", "a")
            f.write(website_credentials)
            f.close()
            password_entry.delete(0, 'end')
            website_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# email/username label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# email/username entry
username_entry = Entry(width=35)
username_entry.insert(END, string="busaria21@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)



# calls action() when pressed
generate_password_button = Button(text="Generate Password", command=generate_password, width=10)
generate_password_button.grid(column=2, row=3)

# add password button

add_button = Button(text="Add", command=add_credentials, width=32)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
