from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
    def move(self):
        y_axis = self.ycor() + 10
        self.goto(self.xcor(), y_axis)
    def finished(self):
        self.goto(STARTING_POSITION)



