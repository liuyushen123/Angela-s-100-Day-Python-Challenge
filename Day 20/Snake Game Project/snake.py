import turtle as t

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_snake()
        self.head_status = "right"
        self.head = self.my_snake[0]
        self.direction_lock = False
    
    def create_snake(self):
        
        for position in [(0,0), (-20,0), (-40,0)]:
            new_segment = t.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.my_snake.append(new_segment)
    
    def create_body(self):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.my_snake[-1].xcor(),self.my_snake[-1].ycor())
        self.my_snake.append(new_segment)

    def move(self):
        for seg in range(1, len(self.my_snake)):
            self.my_snake[-seg].goto(self.my_snake[-seg - 1].xcor(),self.my_snake[-seg - 1].ycor())
        self.my_snake[0].forward(20)
        self.direction_lock = False

    def up(self):
        if self.head_status != "down" and not self.direction_lock:
            self.my_snake[0].setheading(90)
            self.head_status = "up"
            self.direction_lock = True
    
    def down(self):
        if self.head_status != "up" and not self.direction_lock:
            self.my_snake[0].setheading(270)
            self.head_status = "down"
            self.direction_lock = True
    
    def left(self):
        if self.head_status != "right" and not self.direction_lock:
            self.my_snake[0].setheading(180)
            self.head_status = "left"
            self.direction_lock = True

    def right(self):
        if self.head_status != "left" and not self.direction_lock:
            self.my_snake[0].setheading(0)
            self.head_status = "right"
            self.direction_lock = True