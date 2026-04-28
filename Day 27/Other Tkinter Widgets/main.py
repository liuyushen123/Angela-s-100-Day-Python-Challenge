import pygame
import tkinter as tk

pygame.mixer.init()


window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()


def play():
    pygame.mixer.music.load(
        "/Users/liuyuchen/Downloads/General Coding/Dr.Angela Yu's 100Day python challenge/Day 27/Other Tkinter Widgets/resource/Wake Up Hajimi - 哈基米起床.mp3"
    )
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.play()


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())
    play()


button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

input = tk.Entry(width=10)
input.pack()
print(input.get())

window.mainloop()
