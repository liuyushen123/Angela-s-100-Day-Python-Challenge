import random
import tkinter as tk
from tkinter import messagebox

import pyperclip

PLACEHOLDER_EMAIL = "yliu145@example.com"
isGeneratePasswordClicked = False

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Functions


def emailEntry_on_focus_in(event):
    if emailEntry.get() == PLACEHOLDER_EMAIL:
        emailEntry.delete(0, tk.END)
        emailEntry.config(fg="black")
    emailEntry.config(bg="lightyellow")


def emailEntry_on_focus_out(event):
    if emailEntry.get() == "":
        emailEntry.insert(0, PLACEHOLDER_EMAIL)
        emailEntry.config(fg="gray")
        print("用户没有输入任何字符串，重新加载初始字符串")
    else:
        print("用户输入字符串啦！")
    emailEntry.config(bg="white")


def passwordEntry_on_focus_in(event):
    passwordEntry.config(bg="lightyellow")


def passwordEntry_on_focus_out(event):
    passwordEntry.config(bg="white")


def websiteEntry_on_focus_in(event):
    websiteEntry.config(bg="lightyellow")


def websiteEntry_on_focus_out(event):
    websiteEntry.config(bg="white")


def show_copied_msg():
    generatePasswordButton.config(text="Password Copied!", fg="green")
    window.after(
        2000,
        lambda: generatePasswordButton.config(text="Generate Password", fg="black"),
    )


def generate_passowrd(event=None):
    global isGeneratePasswordClicked
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    mPassword = ""

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    for i in range(random.randint(3, 4)):
        mPassword += random.choice(letters)
    for i in range(random.randint(1, 5)):
        mPassword += random.choice(numbers)
    for i in range(random.randint(2, 5)):
        mPassword += random.choice(symbols)

    password_list = list(mPassword)
    random.shuffle(password_list)
    mPassword = "".join(password_list)

    if isGeneratePasswordClicked:
        passwordEntry.delete(0, tk.END)
    passwordEntry.insert(0, mPassword)
    pyperclip.copy(mPassword)
    isGeneratePasswordClicked = True
    show_copied_msg()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    websiteName = websiteEntry.get()
    emailName = emailEntry.get()
    passwordName = passwordEntry.get()

    if (len(websiteName) == 0) or (len(emailName) == 0) or (len(passwordName) == 0):
        messagebox.showinfo(
            title="Empty Field",
            message="Oops make sure to have all of the field filled",
        )
    else:
        is_ok = messagebox.askokcancel(
            title=websiteName,
            message=f"These are the details entered: \nEmail {emailName}"
            f"\nPassword: {passwordName} \n Is it ok to save?",
        )

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{websiteName} | {emailName} | {passwordName} \n")
                websiteEntry.delete(0, tk.END)
                emailEntry.delete(0, tk.END)
                passwordEntry.delete(0, tk.END)
                emailEntry.insert(0, PLACEHOLDER_EMAIL)
                emailEntry.config(fg="gray")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

logo_img = tk.PhotoImage(file="logo.png")

# Lables
websiteLable = tk.Label(text="Website Name: ", bg="white", fg="black")
websiteLable.grid(row=1, column=0)
emailLable = tk.Label(text="Email/Username: ", bg="white", fg="black")
emailLable.grid(row=2, column=0)
passwordLable = tk.Label(text="Password: ", bg="white", fg="black")
passwordLable.grid(row=3, column=0)

# Entries
websiteEntry = tk.Entry(
    bg="white",
    highlightthickness=0,
    cursor="ibeam",
    insertbackground="black",
    borderwidth=1,
    width=34,
    fg="black",
)
websiteEntry.focus()
websiteEntry.grid(row=1, column=1, columnspan=2, sticky="ew")
websiteEntry.bind("<FocusIn>", websiteEntry_on_focus_in)
websiteEntry.bind("<FocusOut>", websiteEntry_on_focus_out)

emailEntry = tk.Entry(
    bg="white",
    highlightthickness=0,
    cursor="ibeam",
    insertbackground="black",
    borderwidth=1,
    fg="gray",
    width=34,
)
emailEntry.bind("<FocusIn>", emailEntry_on_focus_in)
emailEntry.bind("<FocusOut>", emailEntry_on_focus_out)
emailEntry.grid(row=2, column=1, columnspan=2, sticky="ew")
emailEntry.insert(0, "yliu145@example.com")

passwordEntry = tk.Entry(
    bg="white",
    highlightthickness=0,
    cursor="ibeam",
    insertbackground="black",
    borderwidth=1,
    width=21,
    fg="black",
)
passwordEntry.grid(row=3, column=1, sticky="ew")
passwordEntry.bind("<FocusIn>", passwordEntry_on_focus_in)
passwordEntry.bind("<FocusOut>", passwordEntry_on_focus_out)


# Button
generatePasswordButton = tk.Button(
    text="Generate Password",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    cursor="hand2",
    fg="black",
    bg="white",
    highlightbackground="white",
    command=generate_passowrd,
    width=17,
)
generatePasswordButton.grid(row=3, column=2)
addButton = tk.Button(text="Add", highlightbackground="white", width=36, command=save)
addButton.grid(row=4, column=1, columnspan=2)

# Canvas
canvas = tk.Canvas(width=200, height=200, background="white", highlightthickness=0)
canvas.create_image(
    100,
    100,
    image=logo_img,
)

canvas.grid(row=0, column=1)

window.mainloop()
