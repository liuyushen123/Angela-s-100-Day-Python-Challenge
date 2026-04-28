import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.reset()
        

    def go_up(self):
        self.forward(20)
    
    def reset(self):
        self.goto(STARTING_POSITION)
        self.level += 1