import turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.color("black")

    
    def write_score(self, turtle):
        self.clear()
        self.write(f"Level: {turtle.level}",font=FONT)
    
    def write_game_over(self,score):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over! Your final score: {score}", font=FONT,align="center")
