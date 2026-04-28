import turtle
import paddle
import my_ball
import scoreboard
import time

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
turtle.hideturtle()

player_paddle = paddle.Paddle(-380, 0, 2)
player2_paddle = paddle.Paddle(380, 0, 1)

myBall = my_ball.MyBall()
myScoreboard = scoreboard.ScoreBoard(screen.canvheight)
screen.listen()
screen.onkey(player_paddle.go_up, "w")
screen.onkey(player_paddle.go_down, "s")
screen.onkey(player2_paddle.go_up, "Up")
screen.onkey(player2_paddle.go_down, "Down")

while True:
    screen.update()
    myBall.move_my_ball()
    myBall.collustion_y()
    if myBall.xcor() < 0:
        myBall.collusion_x(player_paddle, myScoreboard)

    elif myBall.xcor() > 0:
        myBall.collusion_x(player2_paddle, myScoreboard)


screen.exitonclick()
