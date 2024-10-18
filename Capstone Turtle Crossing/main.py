import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()
    for each_car in car.total_cars: #Looping through the list in which each created car goes. #Car is the object that we created and it has
        #initialized list called total_cars.
        if each_car.distance(player) < 20: #each_car is a turtle object that gets stored in the total_cars after creation of it.
            game_is_on = False
    if player.ycor() == 280: #Successfully reaches the finish line.
        player.finished()
        car.increment()
        scoreboard.update_score()




screen.exitonclick()
