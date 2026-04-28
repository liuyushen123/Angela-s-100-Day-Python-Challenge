import turtle as t
import time

class ScoreBoard (t.Turtle):
    def __init__(self,screen_width):
        super().__init__()
        self.list_of_timmy = [t.Turtle() for _ in range(3)]
        self.width = screen_width
        self.draw_center()

        self.list_of_timmy[1].goto(-150, 200)
        self.list_of_timmy[-1].goto(150,200)
        self.list_of_timmy[1].color('white')
        self.list_of_timmy[-1].color("white")
        self.list_of_timmy[1].hideturtle()
        self.list_of_timmy[-1].hideturtle()
        self.list_of_timmy[1].write(0,font=("Courier",80,"normal"))
        self.list_of_timmy[-1].write(0,font=("Courier",80,"normal"))

    
    def draw_center(self):
        tim = self.list_of_timmy[0]
        tim.penup()
        tim.color("white")
        tim.goto(0,300)
        tim.hideturtle()
        tim.setheading(270)
        tim.pendown()
        tim.width(3)
        for i in range(600 // 20 // 2):
            tim.forward(20)
            tim.penup()
            tim.forward(20)
            tim.pendown()
    def players_score(self, player):
        self.list_of_timmy[player.player_id].clear()
        self.list_of_timmy[player.player_id].write(player.score,font=("Courier",80,"normal"))
    

