from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        


    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(f"{self.l_score}",False, align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(f"{self.r_score}",False, align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",False, align=ALIGNMENT,font=FONT)

    def increase_score_l(self):
            self.l_score += 1
            self.clear()
            self.update_scoreboard()


    
    def increase_score_r(self):
            self.r_score += 1
            self.clear()
            self.update_scoreboard()
