import turtle as t
import time
import random

turtle_colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "black",
    "gray",
    "brown",
    "orange",
    "pink",
    "purple",
    "cyan",
    "magenta",
    "lightblue",
    "lightgreen",
    "lightgray",
    "lightyellow",
    "lightpink",
    "lightsalmon",
    "lightcoral",
    "darkblue",
    "darkgreen",
    "darkred",
    "darkgray",
    "darkcyan",
    "darkorange",
    "darkviolet",
    "gold",
    "silver",
    "tomato",
    "chocolate",
    "maroon",
    "navy",
    "indigo",
    "olive",
    "teal",
    "turquoise",
    "orchid",
    "plum",
]

tim = t.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

turn_degree = 90


def turn(turn_degree):
    tim.left(turn_degree)
    tim.dot(30, random.choice(turtle_colors))
    tim.forward(50)
    tim.left(turn_degree)
    return -turn_degree


for i in range(11):
    for _ in range(10):
        tim.dot(30, random.choice(turtle_colors))
        tim.forward(50)
    turn_degree = turn(turn_degree)


screen = t.Screen()
screen.exitonclick()
