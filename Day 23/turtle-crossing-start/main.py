import random
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
myTurtle = Player()
screen.listen()
screen.onkey(myTurtle.go_up, "w")
myScoreBoard = Scoreboard()
myScoreBoard.write_score(myTurtle)
myManager = CarManager()
myManager.create_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    if myTurtle.ycor() > 290:
        myTurtle.reset()
        myScoreBoard.write_score(myTurtle)
    myManager.move()
    if (len(myManager.carList) < 25) and (1 > random.randint(0, 5)):
        print()
        myManager.create_cars()

    if myManager.collusion_detect(myTurtle):
        for car in myManager.carList:
            car.hideturtle()
        myTurtle.hideturtle()
        myManager.carList = []
        myScoreBoard.write_game_over(myTurtle.level)
        screen.update()
        game_is_on = False
    screen.update()
screen.exitonclick()
