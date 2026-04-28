import turtle as t
import random
import math

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ycoordinate123 = random.randint(-280,280)
        self.xcoordinate123 = random.randint(-280,280)
        self.goto(self.xcoordinate123,self.ycoordinate123)
        self.dot(15,"blue")


    def regenerate(self):
        self.speed("fastest")
        self.clear()
        self.xcoordinate123 = random.randint(-280,280)
        self.ycoordinate123 = random.randint(-280,280)
        self.goto(self.xcoordinate123, self.ycoordinate123)
        self.dot(15,"blue")
        
    def food_collusion(self,snake_head):
        a = (self.ycoordinate123 - snake_head.ycor()) ** 2
        b = (self.xcoordinate123 - snake_head.xcor()) ** 2

        c = math.sqrt(a + b)

        return c