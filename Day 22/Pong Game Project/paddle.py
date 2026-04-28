import turtle

class Paddle(turtle.Turtle):
    def __init__(self,x,y,id):
        super().__init__()
        self.score = 0
        self.player_id = id
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(x,y)
    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)

