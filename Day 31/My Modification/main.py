import random
import tkinter as tk

import pandas as pd
import pygame
import pyperclip
from tkmacosx import Button as MacButton

DESIGNATED_FOLDER_PATH = "images/"
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_PATH_IMG = DESIGNATED_FOLDER_PATH + "card_back.png"
CARD_FRONT_PATH_IMG = DESIGNATED_FOLDER_PATH + "card_front.png"
RIGHT_PATH_IMG = DESIGNATED_FOLDER_PATH + "right.png"
WRONG_PATH_IMG = DESIGNATED_FOLDER_PATH + "wrong.png"
FILE_PATH = "data/medical_terminology_with_chinese_translation.csv"

LIGHT_GREEN = "#7FBF7F"
CARD_BACK_COLOR = "#8FBEAC"

USER_CORRECT = 0
USER_WRONG = 0

window = tk.Tk()
window.title("My Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


data = pd.read_csv(FILE_PATH)
to_learn = data.to_dict(orient="records")
current_card = {}

STATE_QUESTION = "question"
STATE_ANSWER = "answer"
STATE_IDK = "idk"
current_state = STATE_QUESTION
CORRECT_AUDIO = "sounds/duolingo-correct.mp3"

pygame.mixer.init()
SOUND = {
    "correct": pygame.mixer.Sound("sounds/duolingo-correct.mp3"),
    "wrong": pygame.mixer.Sound("sounds/duolingo-wrong.mp3"),
}


def set_state(new_state):
    global current_state
    current_state = new_state

    if new_state == STATE_QUESTION:
        submit_button.config(text="Submit")
        canvas.itemconfig(idk_button, state="normal")
        canvas.coords(green_button, 480, 410)

    elif new_state == STATE_ANSWER:
        submit_button.config(text="Next")

    elif new_state == STATE_IDK:
        submit_button.config(text="Next")
        canvas.itemconfig(idk_button, state="hidden")
        canvas.coords(green_button, 400, 410)


def reset_ui():
    # 卡片翻回正面
    canvas.itemconfig(card_background, image=card_front_img)

    # 标题和文字恢复
    canvas.itemconfig(card_title, text="English", fill="#ABABAB")
    canvas.itemconfig(card_word, fill="black")

    # 输入框恢复
    canvas.itemconfig(entry_window, state="normal")
    answer_entry_text_reset()
    answer_entry.config(fg="black")

    # underline恢复
    canvas.itemconfig(underline, fill="black", width=1, state="normal")
    canvas.itemconfig(green_line, state="hidden")
    canvas.coords(green_line, 300, 365, 500, 365)

    # 按钮恢复
    canvas.coords(green_button, 480, 410)
    canvas.itemconfig(idk_button, state="normal")
    submit_button.config(text="Submit", highlightbackground="white")
    wrong_button.config(highlightbackground="white")


def play_sound(sound_variable):
    SOUND[sound_variable].play()


def get_answer():
    return answer_entry.get().strip().lower()


def sweep(x1=300, x2=500):
    canvas.itemconfig(green_line, state="normal")
    if x1 >= 200 and x2 <= 600:
        canvas.coords(green_line, x1, 365, x2, 365)
        print(x1, x2)
        window.after(5, lambda: sweep(x1 - 10, x2 + 10))


def answer_entry_green_text():
    answer_entry.config(fg=LIGHT_GREEN)


def answer_entry_text_reset():
    answer_entry.configure(fg="black")
    answer_entry.delete(0, tk.END)


def underline_reset():
    canvas.coords(green_line, 300, 365, 500, 365)
    canvas.itemconfig(green_line, state="hidden")


def shake_ui(iteration=0):
    offsets = [15, -15, 13, -13, 11, -11, 10, -10, 8, -8, 6, -6, 4, -4, 2, -2, 0]

    if iteration < len(offsets):
        dist = offsets[iteration]
        canvas.move(card_background, dist, 0)
        canvas.move(card_title, dist, 0)
        canvas.move(card_word, dist, 0)
        canvas.move(underline, dist, 0)
        window.after(25, lambda: shake_ui(iteration + 1))


def next_card(event=None):
    global current_card

    reset_ui()

    current_card = random.choice(to_learn)
    canvas.itemconfig(
        card_word, text=current_card["English Definition"], font=("Arial", 20, "bold")
    )
    set_state(STATE_QUESTION)


def user_got_right(status):
    global USER_CORRECT, USER_WRONG

    if status:
        USER_CORRECT += 1
        canvas.itemconfig(amount_right, text=f"🚀 {USER_CORRECT}")
        return
    USER_CORRECT = 0
    USER_WRONG += 1

    canvas.itemconfig(amount_right, text=f"🚀 {USER_CORRECT}")
    canvas.itemconfig(amount_wrong, text=f"😑 {USER_WRONG}")


def show_answer():
    canvas.itemconfig(card_title, text=current_card["Term"], fill="white")
    canvas.itemconfig(
        card_word,
        text=f"{current_card['English Definition']}\n\n"
        f"{current_card['Chinese Translation']}\n\n"
        f"{current_card['Chinese Definition']}",
        fill="white",
    )
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(underline, state="hidden")
    canvas.itemconfig(entry_window, state="hidden")
    canvas.itemconfig(idk_button, state="hidden")
    canvas.coords(green_button, 400, 410)
    wrong_button.config(highlightbackground=CARD_BACK_COLOR)
    submit_button.config(highlightbackground=CARD_BACK_COLOR, text="Next")


def idk_button_clicked(event=None):
    user_got_right(0)
    show_answer()
    set_state(STATE_IDK)


def check_answer():
    user_input = get_answer()

    if user_input == current_card["Term"].strip().lower():
        play_sound("correct")
        sweep()
        answer_entry_green_text()
        user_got_right(1)
        set_state(STATE_ANSWER)
    else:
        SOUND["wrong"].play()
        window.after(100, shake_ui)
        canvas.itemconfig(underline, fill="#E57373", width=3)
        window.after(500, lambda: canvas.itemconfig(underline, fill="black", width=1))
        user_got_right(0)
        pyperclip.copy(current_card["Term"])


def green_button_clicked(event=None):
    if current_state == STATE_QUESTION:
        check_answer()
        return
    next_card()


canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file=CARD_FRONT_PATH_IMG)
card_back_img = tk.PhotoImage(file=CARD_BACK_PATH_IMG)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
# canvas.bind("<Button-1>", flip_card)
card_title = canvas.create_text(
    400, 150, text="Title", font=("SF Pro", 40, "italic"), fill="#ABABAB"
)

amount_right = canvas.create_text(
    700,
    30,
    font=("Arial", 20, "bold"),
    fill="#4CAF50",
    anchor="e",
    text=f"🚀 {USER_CORRECT}",
)

amount_wrong = canvas.create_text(
    700,
    60,
    font=("Arial", 20, "bold"),
    fill="#E57373",
    anchor="e",
    text=f"😑 {USER_WRONG}",
)

card_word = canvas.create_text(
    400,
    263,
    text="what up",
    font=("Arial", 60, "bold"),
    fill="black",
    width=700,
    justify="center",
)
answer_entry = tk.Entry(
    canvas,
    justify="center",
    background="white",
    font=("Arial", 16),
    highlightthickness=0,
    fg="black",
    width=45,
    insertbackground="black",
    borderwidth=0,
)
answer_entry.focus()
entry_window = canvas.create_window(400, 350, window=answer_entry)
underline = canvas.create_line(200, 365, 600, 365, fill="black", width=1)
submit_button = MacButton(
    canvas,
    text="Submit",
    fg="white",
    bg="#7FBF7F",
    cursor="hand2",
    focuscolor="#7FBF7F",
    highlightbackground="white",
    highlightthickness=0,
    takefocus=0,
    activebackground="#68a368",
    border=0,
    overbackground="#3E9C3E",
    width=120,
    height=40,
    command=green_button_clicked,
)
green_button = canvas.create_window(480, 410, window=submit_button)

green_line = canvas.create_line(
    300, 365, 500, 365, fill="#7FBF7F", width=3, state="hidden"
)

wrong_button = MacButton(
    canvas,
    text="IDK",
    fg="white",
    bg="#E57373",
    activebackground="#D95F5F",
    border=0,
    highlightbackground="white",
    highlightthickness=0,
    overbackground="#DB4F4F",
    width=120,
    height=40,
    command=idk_button_clicked,
)
idk_button = canvas.create_window(320, 410, window=wrong_button)
next_card()

window.mainloop()
