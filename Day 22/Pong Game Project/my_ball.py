import turtle
import time


class MyBall(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(0.5)
        self.penup()
        self.velocity_y = 1
        self.velocity_x = -5

    def move_my_ball(self):
        self.goto(self.xcor() + self.velocity_x, self.ycor() + self.velocity_y)

    def collustion_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.velocity_y = -(self.velocity_y)

    def collusion_x(self, wall1, scoreboard):
        wall1_start = wall1.ycor() + 50
        wall1_end = wall1.ycor() - 50

        if self.xcor() < -363 and self.xcor() > -366:
            if self.ycor() < wall1_start and self.ycor() > wall1_end:
                self.velocity_x = -(self.velocity_x)

        elif self.xcor() > 363 and self.xcor() < 366:
            if self.ycor() < wall1_start and self.ycor() > wall1_end:
                self.velocity_x = -(self.velocity_x)

        elif self.xcor() > 410:
            time.sleep(1)
            self.goto(0, 0)
            wall1.score += 1
            scoreboard.players_score(wall1)
            self.velocity_x = -(self.velocity_x)

        elif self.xcor() < -410:
            time.sleep(1)
            self.goto(0, 0)
            wall1.score += 1
            scoreboard.players_score(wall1)
            self.velocity_x = -(self.velocity_x)
