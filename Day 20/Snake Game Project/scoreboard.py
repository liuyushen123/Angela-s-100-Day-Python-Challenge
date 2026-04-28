import turtle as t

class ScoreBoard (t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write_scoreboard()
        
        
    
    def write_scoreboard(self):
        self.write(f"Score: {self.score}", align="center",font=("Courier",16,"bold"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_scoreboard()
    def game_over(self,mySnake):
        for segment in range(1, len(mySnake.my_snake)):
            if (mySnake.head.distance(mySnake.my_snake[segment]) < 10):
                return False
        return True
    def restart(self):
        self.clear()
        