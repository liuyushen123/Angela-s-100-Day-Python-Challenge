import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.carList = []
    def move(self):
        for car in self.carList:
            car.forward(car.velocity)
            if car.xcor() < -340:
                car.hideturtle()
                self.carList.remove(car)
                
    def create_cars(self):
        adding_car = Car()
        for existing_car in self.carList[:]:
            if existing_car.ycor() == adding_car.ycor():
                return
        self.carList.append(adding_car)
    def collusion_detect(self,player):
        for car in self.carList:
            if car.distance(player) < 20:
                return True
        return False

class Car(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1,3)
        self.setheading(180)
        self.goto(300,random.randint(-250,250))
        self.velocity = random.randint(1,20)




