from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self): #Whenever a new object is initialized all the below gets called automatically.
        super().__init__() #Calling turtle's init here.
        self.shape("circle") #Using the method of turtle but now they also have methods of Food.
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("yellow")
        self.speed(0)
        self.new_location() #Using the method created below to initialze a random location.


    def new_location(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x_axis, y_axis)
