from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Level: {self.level}",align='left', font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.scoreboard()
