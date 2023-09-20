from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score = {self.score}",False, align="center",font=("Arial", 24, "normal"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}",False, align=ALIGNMENT,font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",False, align=ALIGNMENT,font=FONT)

    def increase_score(self):
            self.score += 1
            self.clear()
            self.update_scoreboard()

