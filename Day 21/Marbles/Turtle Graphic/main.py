import random
import turtle

import marble

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor("black")
screen.tracer(0)
marble_list = []


for marbles in range(50):
    marble_list.append(marble.MarbleManager(False, (0, 0, 255)))
for i in marble_list:
    i.goto(random.randint(-280, 280), random.randint(-280, 280))
marble_list.append(marble.MarbleManager(True, (255, 0, 0)))


while True:
    for movingMarb in marble_list:
        if movingMarb.stuck:
            for trueMarb in marble_list:
                if not trueMarb.stuck:
                    movingMarb.collusion(trueMarb)
        if movingMarb.flash:
            movingMarb.flash -= 5
            print(movingMarb.flash)
            movingMarb.color_update()

        movingMarb.moving()
    for i in range(len(marble_list)):
        for j in range(i + 1, len(marble_list)):
            if (
                (marble_list[i].stuck is not True)
                and (marble_list[j].stuck is not True)
                and marble_list[i].distance(marble_list[j]) < 15
            ):
                marble_list[i].velocity_x, marble_list[j].velocity_x = (
                    marble_list[j].velocity_x,
                    marble_list[i].velocity_x,
                )
                marble_list[i].velocity_y, marble_list[j].velocity_y = (
                    marble_list[j].velocity_y,
                    marble_list[i].velocity_y,
                )

            if (marble_list[i].stuck) and (marble_list[j].stuck):
                marble_list[i].vibration(marble_list[j])
                marble_list[j].vibration(marble_list[i])
    for i in marble_list:
        if not (i.flash):
            i.has_vibrated = False

    screen.update()

screen.exitonclick()
