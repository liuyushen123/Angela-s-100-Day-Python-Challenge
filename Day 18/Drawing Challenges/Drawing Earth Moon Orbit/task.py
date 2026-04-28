import turtle as t
import math
import time


earth = t.Turtle()
moon = t.Turtle()
moon_circle = t.Turtle()

moon_circle.shape("circle")
earth.shape("circle")
moon.shape("circle")

moon_circle.penup()
earth.penup()
moon.penup()


while True:
    for i in range(365):
        x = 50 * (4 * math.cos((2 * math.pi / 365) * i))
        y = 50 * (4 * math.sin((2 * math.pi / 365) * i))
        moon_x = 50 * (
            2 * math.cos((2 * math.pi / 28) * i) + 4 * math.cos((2 * math.pi / 365) * i)
        )
        moon_y = 50 * (
            2 * math.sin((2 * math.pi / 28) * i) + 4 * math.sin((2 * math.pi / 365) * i)
        )

        earth.goto(x, y)
        moon.goto(moon_x, moon_y)


screen = t.Screen()
screen.exitonclick
