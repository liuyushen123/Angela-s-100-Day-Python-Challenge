import random
import turtle

import ballmanager

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball Simulator")
screen.setup(width=800, height=800)
screen.tracer(0)
ball_list = []

for i in range(20):
    new_ball = ballmanager.BallManager()
    for existing_ball in ball_list:
        while new_ball in ball_list:
            new_ball.goto(random.randint(-390, 390), random.randint(200, 400))
    ball_list.append(new_ball)
gravity = 0.1
velocity_y = 2
velocity_x = 2

while True:
    for ball in ball_list:
        ball.move()

    for x in range(0, len(ball_list)):
        for y in range(x + 1, len(ball_list)):
            ball_list[x].collusion(ball_list[y])
    screen.update()


screen.exitonclick()
