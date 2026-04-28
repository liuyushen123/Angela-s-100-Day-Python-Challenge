import math
import random
import time
import tkinter as tk

root = tk.Tk()

W = 800
H = 600


g = print("%d%d", (W, H))
root.geometry(g)
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width=W, height=H)
root.title("Bunch of Marble")
SIZE = 14.5


def dec2hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


class Marble:
    def __init__(self, x, y, stuck, r, g, b, velocity):
        self.x = x
        self.y = y
        self.vely = velocity
        self.velx = velocity
        self.y2 = self.y + SIZE
        self.x2 = self.x + SIZE
        self.stuck = stuck
        self.red = r
        self.green = g
        self.blue = b
        self.vibrate = 0
        self.vibrated = False
        s = 1
        if s == 0:
            self.shape = "square"
        if s == 1:
            self.shape = "circle"

    def draw(self):
        r = self.red + self.vibrate * 4
        if r > 255:
            r = 255
        g = self.green + self.vibrate * 4
        if g > 255:
            g = 255
        b = self.blue + self.vibrate * 4
        if b > 255:
            b = 255
        if self.shape == "square":
            canvas.create_rectangle(
                [self.x, self.y, self.x + SIZE, self.y + SIZE],
                fill=dec2hex(r, g, b),
                outline="",
            )
        else:
            canvas.create_oval(
                [self.x, self.y, self.x + SIZE, self.y + SIZE],
                fill=dec2hex(r, g, b),
                outline="",
            )

    def move(self):
        if self.stuck:
            self.velx = 0
            self.vely = 0

        self.x += self.velx
        self.y += self.vely

        if self.x + SIZE > W:
            self.velx = -self.velx
        if self.y + SIZE > H:
            self.vely = -self.vely
        if self.x < 0:
            self.velx = -self.velx
        if self.y < 0:
            self.vely = -self.vely

    def collusion(self, other_marble):
        a = self.x - other_marble.x
        b = self.y - other_marble.y
        c = math.sqrt((a**2) + (b**2))
        if self.shape == "circle":
            if c <= SIZE and other_marble.stuck is not True:
                other_marble.stuck = True
                other_marble.red = self.red + 10
                other_marble.green = self.green - 10
                other_marble.blue = self.blue - 10
                if other_marble.red >= 255:
                    other_marble.red = 255
                if other_marble.green >= 255:
                    other_marble.green = 255
                if other_marble.blue >= 255:
                    other_marble.blue = 255
                if other_marble.red <= 0:
                    other_marble.red = 0
                if other_marble.green <= 0:
                    other_marble.green = 0
                if other_marble.blue <= 0:
                    other_marble.blue = 0
                other_marble.vibrate = 30
                other_marble.vibrated = True

        if (self.stuck) and (other_marble.stuck) and c <= SIZE:
            if other_marble.vibrate == 25 and self.vibrated is not True:
                self.vibrate = 30
                self.vibrated = True


list_of_Marbles = []


list_of_Marbles.append(Marble(W / 2, H / 2, True, 1, 150, 32, 0))
for y in range(1, 60):
    x = random.randint(50, 500)
    y = random.randint(50, 400)
    velocity = random.randint(-3, 5)
    if velocity == 0:
        velocity = 3
    elif velocity == -1:
        velocity = -2
    elif velocity == 1:
        velocity = 2

    list_of_Marbles.append(Marble(x, y, False, 0, 255, 255, velocity))


while True:
    for i in list_of_Marbles:
        if i.stuck and i.vibrate < 0:
            i.vibrated = False

    stuck_marbles = 0

    canvas.delete("all")
    canvas["bg"] = "black"
    for i in range(len(list_of_Marbles)):
        if list_of_Marbles[i].stuck is not True:
            stuck_marbles += 1
    if stuck_marbles == 0:
        for y in range(1, 25):
            x = random.randint(13, 500)
            y = random.randint(13, 400)
            velocity = random.randint(-5, 10)
            if velocity == 0:
                velocity = 3
            elif velocity == -1:
                velocity = -2
            elif velocity == 1:
                velocity = 2
            list_of_Marbles.append(Marble(x, y, False, 0, 255, 255, velocity))

    for y in range(len(list_of_Marbles)):
        if list_of_Marbles[y].stuck:
            for x in range(len(list_of_Marbles)):
                if list_of_Marbles[x].stuck is not True:
                    list_of_Marbles[y].collusion(list_of_Marbles[x])

    for y in list_of_Marbles:
        if y.vibrate == 0:
            y.vibrated = False

    for i in list_of_Marbles:
        if i.vibrate > 0:
            i.vibrate -= 1

    for y in range(len(list_of_Marbles)):
        if list_of_Marbles[y].stuck:
            for x in range(len(list_of_Marbles)):
                if x != y:
                    if list_of_Marbles[x].stuck:
                        list_of_Marbles[y].collusion(list_of_Marbles[x])

    for i in range(len(list_of_Marbles)):
        list_of_Marbles[i].draw()
        list_of_Marbles[i].move()
    canvas.update()

    time.sleep(0.01)


##If a ball hits a color ball the ball will stay white. If hits a white ball color will fade
