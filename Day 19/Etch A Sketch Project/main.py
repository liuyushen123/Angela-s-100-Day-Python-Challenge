import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forwads():
    tim.forward(10)
def move_up():
    tim.rt(10)
def move_backward():
    tim.backward(10)
def move_down():
    tim.lt(10)

screen.listen()
screen.onkey(move_forwads, "w")
screen.onkey(move_up, "d")
screen.onkey(move_down, "a")
screen.onkey(move_backward, "s")
screen.update()

screen.exitonclick()