from turtle import Turtle, Screen, pos, end_fill,color , forward, right, left
import time

distance = 10
num_size = 3

while True:

    degree = 360 / num_size
    for i in range(num_size):
        forward(distance)
        right(degree)
    num_size += 1

screen = Screen()
screen.exitonclick()