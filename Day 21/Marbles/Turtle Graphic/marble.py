import turtle
import random


class MarbleManager(turtle.Turtle):
    def __init__(self, stuck, color_tuple):
        super().__init__()
        self.shape("circle")
        turtle.colormode(255)
        self.penup()
        self.shapesize(0.5)
        self.rgb_color = color_tuple
        self.color(color_tuple)
        self.velocity_y = random.choice([-1, 1, -2, 2])
        self.velocity_x = random.choice([-1, 1, -2, 2])
        self.stuck = stuck
        self.flash = 0
        self.has_vibrated = False

    def moving(self):
        if self.stuck:
            self.velocity_x = 0
            self.velocity_y = 0

        if self.ycor() < -285 or self.ycor() > 290:
            self.velocity_y *= -1
        if self.xcor() < -285 or self.xcor() > 285:
            self.velocity_x *= -1

        self.goto(self.xcor() + self.velocity_x, self.ycor() + self.velocity_y)

    def find_right_number(self):
        return tuple(max(0, min(255, v)) for v in self.rgb_color)

    def collusion(self, moving_marble):
        if self.distance(moving_marble) < 13:
            moving_marble.stuck = True
            moving_marble.flash = 150
            moving_marble.rgb_color = (
                self.rgb_color[0] - 20,
                self.rgb_color[1] + 15,
                self.rgb_color[2] + 20,
            )
            moving_marble.has_vibrated = True

        moving_marble.rgb_color = moving_marble.find_right_number()
        moving_marble.color(moving_marble.rgb_color)

    def color_update(self):
        r, g, b = self.rgb_color
        display_color = (r + self.flash, g + self.flash, b + self.flash)
        self.color(tuple(max(0, min(255, v)) for v in display_color))

    def vibration(self, other):
        if (
            self.stuck
            and other.stuck
            and self.flash == 135
            and other.flash == 0
            and not other.has_vibrated
            and self.distance(other) < 13
        ):
            other.flash = 150
            other.has_vibrated = True
