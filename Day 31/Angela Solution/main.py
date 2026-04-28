import random
import tkinter as tk

import pandas as pd

DESIGNATED_FOLDER_PATH = "images/"
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_PATH_IMG = DESIGNATED_FOLDER_PATH + "card_back.png"
CARD_FRONT_PATH_IMG = DESIGNATED_FOLDER_PATH + "card_front.png"
RIGHT_PATH_IMG = DESIGNATED_FOLDER_PATH + "right.png"
WRONG_PATH_IMG = DESIGNATED_FOLDER_PATH + "wrong.png"
FILE_PATH = "data/french_words.csv"
is_front = True

data = pd.read_csv(FILE_PATH)
to_learn = data.to_dict(orient="records")
current_card = {}


def button_clicked(event=None):
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


def flip_card(event=None):
    global is_front

    if is_front:
        canvas.itemconfig(card_title, text="English")
        canvas.itemconfig(card_word, text=current_card["English"])
        canvas.itemconfig(card_background, image=card_back_img)
        canvas.itemconfig(card_title, fill="white")
        canvas.itemconfig(card_word, fill="white")
    else:
        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(card_word, text=current_card["French"])
        canvas.itemconfig(card_background, image=card_front_img)
        canvas.itemconfig(card_title, fill="black")
        canvas.itemconfig(card_word, fill="black")
    is_front = not is_front


window = tk.Tk()
window.title("My Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file=CARD_FRONT_PATH_IMG)
card_back_img = tk.PhotoImage(file=CARD_BACK_PATH_IMG)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
canvas.bind("<Button-1>", flip_card)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Arial", 40, "italic"), fill="black"
)
card_word = canvas.create_text(
    400, 263, text="trouve", font=("Arial", 60, "bold"), fill="black"
)

cross_image = tk.PhotoImage(file=WRONG_PATH_IMG)
unknown_button = tk.Button(
    image=cross_image,
    highlightthickness=0,
    borderwidth=0,
    relief="flat",
    bg=BACKGROUND_COLOR,
)
unknown_button.grid(row=1, column=0)
unknown_button.config(highlightthickness=0)

check_img = tk.PhotoImage(file=RIGHT_PATH_IMG)
known_button = tk.Button(
    image=check_img,
    highlightthickness=0,
    borderwidth=0,
    relief="flat",
    bg=BACKGROUND_COLOR,
    bd=0,
    activebackground=BACKGROUND_COLOR,
    command=button_clicked,
)
known_button.grid(row=1, column=1)
button_clicked()


window.mainloop()
