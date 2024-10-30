from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong Game")

r_paddle = Paddle((350, 0)) #Takes tuple as an input
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
scoreboard = Scoreboard()

game_on = True
sleep_time = 0.08
while game_on:
    time.sleep(sleep_time)
    ball.move()


    #Detecting the collisions.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #Detecting collision with right and left paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        sleep_time *= 0.9 #It will never go negative.
    if ball.xcor() > 380: #This detects when the paddle misses the ball on right side.
        ball.ball_reset()
        scoreboard.increase_l()
        sleep_time = 0.08
    if ball.xcor() < -380:
        ball.ball_reset() #Doing this separately so that points can be calculated.
        scoreboard.increase_r()
        sleep_time = 0.08 #This can also be done the in the ball class. See comments.

    screen.update()
















screen.exitonclick()
