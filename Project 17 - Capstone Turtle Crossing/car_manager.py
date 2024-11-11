import random
from ctypes import memmove
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.total_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car = random.randint(1, 6)
        if random_car == 1: #Only makes the car if we get 1. Method will run every time in while loop but only make car when 6 comes.
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            y_axis = random.randint(-250, 250)
            new_car.goto(300, y_axis)
            self.total_cars.append(new_car)

    def move(self):
        for cars in self.total_cars:
            cars.backward(self.car_speed)
    def increment(self):
        self.car_speed += MOVE_INCREMENT
        self.move()


