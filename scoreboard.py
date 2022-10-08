from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-10, 270)
        self.print_score(p1_score=0, p2_score=0)

    def print_score(self, p1_score, p2_score):
        self.clear()
        self.goto(-10, 270)
        self.write(f"{p1_score} : {p2_score}", True,align="center", font=("Arial", 30, "normal"))

    def game_over_screen(self, p1_score, p2_score):
        self.clear()
        self.goto(-10, 0)
        self.write(f"GAME OVER \n"
                   f"        {p1_score} : {p2_score}", True, align="center", font=("Arial", 30, "normal"))
