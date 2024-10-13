from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.currentscore = 0
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.currentscore}", False, align ="center", font=('arial', 14, 'normal'))
        self.hideturtle()

    def new_score(self):
        self.currentscore += 1
        self.clear()
        self.write(f"Score: {self.currentscore}", False, align="center", font=('arial', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('arial', 14, 'normal'))

