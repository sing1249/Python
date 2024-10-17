from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()


    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        #self.ball_speed = 0.1

    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_core= self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_core)

    def wall_bounce(self):
        self.y_move *= -1 #Reverses the current y_move, positive turns to negative and negative turns to positive.
    def paddle_bounce(self):
        self.x_move *= -1 #Reverses the current x_move.
        #self.ball_speed *= 0.9
    def ball_reset(self):
        self.goto(0, 0)
        self.x_move *= -1 #Reverses the x-axis so that it goes to the opposite player.
        #self.ball_speed = 0.1
