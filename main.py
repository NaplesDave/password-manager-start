from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# David King  May 12, 2022  Password Generator / Manager program
# Udemy - London App Brewery - Python 100 days of code 2022 course

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # using LIST COMPREHENSION to make item lists
    password_letters = [choice(letters) for _ in range(randint(8, 10))]  # set number of letters in password
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]  # set number of symbols in password
    password_numbers = [choice(numbers) for _ in range(randint(8, 10))]  # set number of numbers in password

    password_list = password_letters + password_symbols + password_numbers  # combine lists into one

    shuffle(password_list)  # mix the characters up

    password = "".join(password_list)  # convert the LIST items into one String with join

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)  # put new password on clipboard for quick paste


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get data from entry fields and save it to local vars
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:  # check for empty data entries
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty")
    else:
        # fields are not empty, go ahead and save the data
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Clear entry fields after save
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()  # put cursor back in entry field for next item

            with open("data.txt", "a") as data_file:  # open data file in append mode
                data_file.write(f"{website} | {email} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #
# create program window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# create canvas in window to place items

canvas = Canvas(height=200, width=200, highlightthickness=0)  # create canvas to work on

# convert image and place on canvas for Logo for program
logo_img = PhotoImage(file="logo.png")  # convert png to a Tkinter image
canvas.create_image(100, 100, image=logo_img)  # set image name and position on canvas
canvas.grid(column=0, row=0, columnspan=3)  # Show image in window

# create and place other interface items like labels and entry items and buttons
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(0, "k2_daveking@hotmail.com")  # default address added
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=gen_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()  # keep window open
