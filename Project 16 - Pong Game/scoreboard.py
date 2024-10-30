from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-100, 200)
        self.write(self.left_score, align = "center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def increase_l(self):
        self.left_score += 1
        self.clear()
        self.write_score()
    def increase_r(self):
        self.right_score += 1
        self.clear()
        self.write_score()
