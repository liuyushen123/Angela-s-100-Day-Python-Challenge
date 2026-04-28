import turtle as t
import time
import snake
import food
import scoreboard


def restart_game():
    new_scoreboard.restart()
    game()


def game():
    screen = t.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()
    mySnake = snake.Snake()
    myFood = food.Food()
    myScoreboard = scoreboard.ScoreBoard()
    screen.onkey(mySnake.up,"w")
    screen.onkey(mySnake.down,"s")
    screen.onkey(mySnake.right,"d")
    screen.onkey(mySnake.left,"a")
    
    is_game_over = True

    while is_game_over:
        screen.update()
        time.sleep(0.1)
        mySnake.move()

        if (mySnake.head.xcor() > 290) or (mySnake.head.xcor() < -290):
            mySnake.head.goto(-(mySnake.head.xcor()) , mySnake.head.ycor())
        
        if (mySnake.head.ycor() > 290) or (mySnake.head.ycor() < -290):
            mySnake.head.goto(mySnake.head.xcor() , -(mySnake.head.ycor()))
        if (myFood.food_collusion(mySnake.head) < 20):
            myScoreboard.increase_score()
            myFood.regenerate()
            mySnake.create_body()

        is_game_over = myScoreboard.game_over(mySnake)

    time.sleep(1)
    global new_scoreboard
    new_scoreboard = scoreboard.ScoreBoard()
    myScoreboard.clear()
    for segment in mySnake.my_snake:
        segment.hideturtle()

    myFood.clear()
    new_scoreboard.goto(0,0)
    new_scoreboard.write("Game over!", align="center",font=("Courier",16,"bold"))
    new_scoreboard.goto(0,-30)
    new_scoreboard.write(f"Your final score: {myScoreboard.score}", align="center",font=("Courier",16,"bold"))
    new_scoreboard.goto(0,-60)
    new_scoreboard.write("Press 'r' to restart the game", align="center",font=("Courier",16,"bold"))


    screen.onkey(restart_game,"r")
    screen.update()
    screen.exitonclick()
    

        
        

game()
