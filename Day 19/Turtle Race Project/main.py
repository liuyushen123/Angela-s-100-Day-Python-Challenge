import turtle as t
import random

screen = t.Screen()
color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
screen.setup(width=500,height=700)

is_going = True
turtle_list = [t.Turtle() for _ in range(6)]




for i, x in enumerate(turtle_list):
    x.penup()
    x.shape("turtle")
    x.color(color_list[i])
    x.goto(-230, 100 - i * 80)
while is_going:
    

    for i in turtle_list:
        if i.xcor() > 230:
            winning_color = i.pencolor()
            print(f"{winning_color} is the winner!")
            is_going = False
        i.forward(random.randint(1,20))

screen.exitonclick()
