import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(bg="white")


input = tk.Entry(
    window,
    width=8,
    bg="white",
    bd=0,
    highlightthickness=1,
    highlightcolor="black",
    insertbackground="black",
    fg="black",
)


my_lable = tk.Label(
    text=" = ",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="black",
)

result_lable = tk.Label(
    text="18",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="black",
)


def get_result(event):
    try:
        miles = float(input.get())
        km = miles * 1.60934
        result_lable.config(text=f"{km:.3f}")
    except ValueError:
        result_lable.config(text="-")


tk.Label(window, text="", fg="white", bg="white").grid(row=0, column=0)
tk.Label(window, text="", fg="white", bg="white").grid(row=1, column=0)
tk.Label(window, text="", fg="white", bg="white").grid(row=2, column=1)
tk.Label(window, text="", fg="white", bg="white").grid(row=2, column=2)
tk.Label(window, text="", fg="white", bg="white").grid(row=2, column=3)
tk.Label(window, text="Miles", fg="black", bg="white").grid(row=2, column=7)
tk.Label(window, text="Km", fg="black", bg="white").grid(row=2, column=12)

input.grid(column=4, row=2)
my_lable.grid(column=10, row=2)
result_lable.grid(column=11, row=2)

input.focus()
input.bind("<KeyRelease>", get_result)


window.mainloop()
