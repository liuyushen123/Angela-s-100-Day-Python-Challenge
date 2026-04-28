import json
import random
import tkinter as tk
from tkinter import messagebox

import pyperclip

# =========================================================
# CONSTANTS
# =========================================================

ROW_PADDING = 5
PLACEHOLDER_EMAIL = "yliu145@example.com"


# =========================================================
# UI HELPER FUNCTIONS
# =========================================================


def highlight_entry(event):
    """Highlight entry when focused"""
    event.widget.config(bg="lightyellow")


def unhighlight_entry(event):
    """Return entry color when focus lost"""
    event.widget.config(bg="white")


def show_copied_msg():
    """Show temporary message when password copied"""
    generatePasswordButton.config(text="Password Copied!", fg="green")

    window.after(
        1000,
        lambda: generatePasswordButton.config(text="Generate Password", fg="black"),
    )


# =========================================================
# EMAIL ENTRY PLACEHOLDER LOGIC
# =========================================================


def emailEntry_on_focus_in(event):
    if emailEntry.get() == PLACEHOLDER_EMAIL:
        emailEntry.delete(0, tk.END)
        emailEntry.config(fg="black")

    highlight_entry(event)


def emailEntry_on_focus_out(event):
    if emailEntry.get() == "":
        emailEntry.insert(0, PLACEHOLDER_EMAIL)
        emailEntry.config(fg="gray")
        print("用户没有输入任何字符串，重新加载初始字符串")
    else:
        print("用户输入字符串啦！")

    unhighlight_entry(event)


# =========================================================
# PASSWORD GENERATOR
# =========================================================


def generate_password(event=None):
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

    # Generate password components
    for i in range(random.randint(5, 10)):
        mPassword += random.choice(letters)

    for i in range(random.randint(5, 8)):
        mPassword += random.choice(numbers)

    for i in range(random.randint(5, 8)):
        mPassword += random.choice(symbols)

    # Shuffle password
    password_list = list(mPassword)
    random.shuffle(password_list)
    mPassword = "".join(password_list)

    passwordEntry.delete(0, tk.END)
    passwordEntry.insert(0, mPassword)

    pyperclip.copy(mPassword)

    isGeneratePasswordClicked = True
    show_copied_msg()


# =========================================================
# DATA FUNCTIONS
# =========================================================


def load_data():
    """Load JSON data file"""
    try:
        with open("data.json", "r") as f:
            return json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def reset_fields():
    """Clear input fields"""
    websiteEntry.delete(0, tk.END)
    emailEntry.delete(0, tk.END)
    passwordEntry.delete(0, tk.END)

    emailEntry.insert(0, PLACEHOLDER_EMAIL)
    emailEntry.config(fg="gray")


# =========================================================
# SAVE PASSWORD
# =========================================================


def save():
    websiteName = websiteEntry.get().strip().title()
    emailName = emailEntry.get().strip()
    passwordName = passwordEntry.get().strip()
    prompt_message = f"These are the details entered: \nEmail {emailName}\nPassword: {passwordName} \nIs it ok to save?"
    if (len(websiteName) == 0) or (len(emailName) == 0) or (len(passwordName) == 0):
        messagebox.showinfo(
            title="Empty Field",
            message="Oops make sure to have all of the field filled",
        )
        return
    if websiteName in jsonData:
        prompt_message = f"A password is already saved for {websiteName}. Do you want to update the existing entry"

    is_ok = messagebox.askokcancel(
        title=websiteName,
        message=prompt_message,
    )

    if not is_ok:
        return

    new_data = {
        websiteName: {
            "email": emailName,
            "password": passwordName,
        }
    }

    print(new_data[websiteName])

    jsonData.update(new_data)

    with open("data.json", "w") as f:
        json.dump(jsonData, f, indent=4, sort_keys=True)

    reset_fields()


# =========================================================
# SEARCH PASSWORD
# =========================================================


def find_password():

    wanted_website = websiteEntry.get().title().strip()

    if wanted_website == "":
        messagebox.showinfo(
            title="Error", message="Please enter a website name to search."
        )
        return

    if wanted_website in jsonData:
        email = jsonData[wanted_website]["email"]
        password = jsonData[wanted_website]["password"]
        messagebox.showinfo(
            title=wanted_website,
            message=f"Website: {wanted_website}\nEmail: {email}\nPassword: {password}",
        )
    else:
        messagebox.showerror(title="Error", message="Website Not Found!")


# =========================================================
# MAIN WINDOW SETUP
# =========================================================

window = tk.Tk()

window.title("Password Manager")

window.config(padx=50, pady=50, bg="white")

logo_img = tk.PhotoImage(file="logo.png")


# =========================================================
# LABELS
# =========================================================

websiteLable = tk.Label(text="Website Name: ", bg="white", fg="black", pady=ROW_PADDING)

websiteLable.grid(row=1, column=0, sticky="e ns")

emailLable = tk.Label(text="Email/Username: ", bg="white", fg="black", pady=ROW_PADDING)

emailLable.grid(row=2, column=0)

passwordLable = tk.Label(text="Password: ", bg="white", fg="black", pady=ROW_PADDING)

passwordLable.grid(row=3, column=0, sticky="e")


# =========================================================
# ENTRY FIELDS
# =========================================================

websiteEntry = tk.Entry(
    bg="white",
    highlightthickness=0,
    cursor="ibeam",
    insertbackground="black",
    borderwidth=1,
    width=21,
    fg="black",
)

websiteEntry.focus()

websiteEntry.grid(row=1, column=1, pady=ROW_PADDING, sticky="w ns")

websiteEntry.bind("<FocusIn>", highlight_entry)
websiteEntry.bind("<FocusOut>", unhighlight_entry)


emailEntry = tk.Entry(
    bg="white",
    highlightthickness=0,
    cursor="ibeam",
    insertbackground="black",
    borderwidth=1,
    fg="gray",
    width=21,
)

emailEntry.grid(row=2, column=1, pady=ROW_PADDING, columnspan=2, sticky="ew")

emailEntry.insert(0, "yliu145@example.com")

emailEntry.bind("<FocusIn>", emailEntry_on_focus_in)
emailEntry.bind("<FocusOut>", emailEntry_on_focus_out)


passwordEntry = tk.Entry(
    bg="white",
    highlightthickness=0,
    cursor="ibeam",
    insertbackground="black",
    borderwidth=1,
    fg="black",
    width=21,
)

passwordEntry.grid(row=3, column=1, sticky="w", pady=ROW_PADDING)

passwordEntry.bind("<FocusIn>", highlight_entry)
passwordEntry.bind("<FocusOut>", unhighlight_entry)


# =========================================================
# BUTTONS
# =========================================================

generatePasswordButton = tk.Button(
    text="Generate Password",
    relief="groove",
    cursor="hand2",
    fg="black",
    bg="#f0f0f0",
    highlightbackground="white",
    command=generate_password,
    width=17,
)

generatePasswordButton.grid(row=3, column=2, sticky="e", pady=(0, ROW_PADDING))


addButton = tk.Button(
    text="Add",
    highlightbackground="white",
    command=save,
)

addButton.grid(row=4, column=1, columnspan=2, sticky="ew")


searchButton = tk.Button(
    text="Search",
    highlightthickness=0,
    relief="groove",
    cursor="hand2",
    fg="black",
    bg="white",
    highlightbackground="white",
    width=17,
    command=find_password,
)

searchButton.grid(row=1, column=2, sticky="e", pady=(0, ROW_PADDING))


# =========================================================
# CANVAS (LOGO)
# =========================================================

canvas = tk.Canvas(width=200, height=200, background="white", highlightthickness=0)

canvas.create_image(55, 100, image=logo_img)

canvas.grid(row=0, column=1, columnspan=2)


# =========================================================
# LOAD JSON DATA
# =========================================================

jsonData = load_data()

print(jsonData)


# =========================================================
# START PROGRAM
# =========================================================

window.mainloop()
