from turtle import Turtle, Screen, pos, end_fill,color , forward, right
import time
import random

turtle_colors = [
    "red", "green", "blue", "yellow", "black", "white", "gray",
    "brown", "orange", "pink", "purple", "cyan", "magenta",
    "lightblue", "lightgreen", "lightgray", "lightyellow",
    "lightpink", "lightsalmon", "lightcoral",
    "darkblue", "darkgreen", "darkred", "darkgray",
    "darkcyan", "darkorange", "darkviolet",
    "gold", "silver", "tomato", "chocolate",
    "maroon", "navy", "indigo", "olive",
    "teal", "turquoise", "orchid", "plum"
]

timmy = Turtle()
timmy.speed("fastest")

for _ in range(360):
    timmy.color(random.choice(turtle_colors))
    timmy.circle(100)
    timmy.setheading((5 * _) + 5)
screen = Screen()
screen.exitonclick()