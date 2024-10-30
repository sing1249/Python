import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("DarkSlateBlue")
screen.title("Snake Game")
screen.tracer(0) #Stops the animation and then later continued with screen.update
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update() #It will move all the snake segments together as it executes after each for loop.
    time.sleep(0.1) #Slows down the movement from default behaviour.
    snake.move() #Snake move every time the screen refreshes

    if snake.head.distance(food) < 15: #snake.head is the first block of the snake. distance method used to check distance b/w food.
        food.new_location() #generated a new random location for the food.
        score.new_score()
        snake.after_food()
    # Detecting location with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
    # Detecting the collision with tale. i.e. head colliding with tale.
    for blocks in snake.squareblocks[1:]: #Skips the first block using slice.
        if snake.head.distance(blocks) < 10:
            game_on = False
            score.game_over()

























screen.exitonclick()
