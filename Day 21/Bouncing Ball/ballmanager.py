import random
import turtle

SHAPES = ["circle", "triangle", "square"]

COLORS = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "white",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "lime",
    "violet",
    "turquoise",
    "salmon",
    "coral",
    "beige",
    "chocolate",
    "crimson",
    "lightgray",
    "lightblue",
    "lightgreen",
    "lavender",
    "plum",
    "orchid",
]


class BallManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.vx = random.choice([-1, 1, -2, 2, 3, -3])
        self.vy = 0
        self.gravity = 0.1
        self.rotate = random.choice([-1, 1, -2, 2, 3, -3])

        self.color(random.choice(COLORS))
        self.shape(random.choice(SHAPES))
        self.penup()
        self.goto(random.randint(-390, 390), random.randint(200, 400))

    def move(self):
        self.vy -= self.gravity
        self.rt(self.rotate)
        if self.ycor() < -390:
            self.sety(-390)
            self.vy = -(self.vy)
            self.rotate = -(self.rotate)
        if (self.xcor() < -400) or (self.xcor() > 400):
            self.vx = -(self.vx)
            self.rotate = -(self.rotate)

        self.goto(self.xcor() + self.vx, self.ycor() + self.vy)

    def collusion(self, other):

        if self.distance(other) < 30:
            current_dist = self.distance(other)

            next_self_x = self.xcor() + self.vx
            next_self_y = self.ycor() + self.vy
            next_other_x = other.xcor() + other.vx
            next_other_y = other.ycor() + other.vy
            future_dist = (
                (next_self_x - next_other_x) ** 2 + (next_self_y - next_other_y) ** 2
            ) ** 0.5

            if future_dist < current_dist:
                self.vx, other.vx = other.vx, self.vx
                self.vy, other.vy = other.vy, self.vy
