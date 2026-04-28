import tkinter as tk

MIN = 00
SEC = 00
timer = None

PATH = "/Users/liuyuchen/Downloads/General Coding/Udemy Course/AngelaYu_100DaysPython/Day 28/Amazing Digital Circus Fish Count Down/hq720.png"

window = tk.Tk()
window.title("Dude they took everything!")
window.config()


def left_button(event):
    global MIN
    MIN += 1
    canvas.itemconfig(timer_text, text=f"{MIN:02d}:{SEC:02d}")


def right_button(event):
    global SEC, MIN

    SEC += 15
    if SEC >= 60:
        SEC = 0
        MIN += 1
    canvas.itemconfig(timer_text, text=f"{MIN:02d}:{SEC:02d}")


def count_down(event=None):
    global MIN, SEC, timer
    print("Going in")
    if (MIN == 0) and (SEC == 0):
        return
    elif (MIN != 0) and (SEC <= 0):
        MIN -= 1
        SEC = 59
    else:
        SEC -= 1
    canvas.itemconfig(timer_text, text=f"{MIN:02d}:{SEC:02d}")
    timer = window.after(1000, count_down)


def reset_timer(event=None):
    global MIN, SEC, timer
    print("Reseting")
    if timer is not None:
        window.after_cancel(timer)
        MIN, SEC = 0, 0
        canvas.itemconfig(timer_text, text=f"{MIN:02d}:{SEC:02d}")


canvas = tk.Canvas(width=680, height=390)
fish_img = tk.PhotoImage(file=PATH)
canvas.create_image(340, 200, image=fish_img)
canvas.pack(fill="both", expand=True)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.pack()

start_button = tk.Button(text="Start", highlightthickness=0, command=count_down)
start_button.pack()

canvas.create_rectangle(150, 90, 260, 140, outline="", fill="", tags="left")
canvas.create_rectangle(450, 90, 560, 140, outline="", fill="", tags="right")

canvas.tag_bind("left", "<Button-1>", left_button)
canvas.tag_bind("right", "<Button-1>", right_button)

timer_text = canvas.create_text(
    340, 260, text=f"{00}:{00}", fill="white", font=("Arial", 24), tags="timer"
)


window.mainloop()
