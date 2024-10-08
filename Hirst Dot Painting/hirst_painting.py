# EXTRACTING THE COLORS FROM IMAGE
# import colorgram
#
# colors = colorgram.extract('Image.jpg', 30)
#
# print(colors) #Colors are in a list and in order to access rgb value we will use .rgb
# rgb_colors = [] #Making an empty list.
# for a in colors: #For each color, appending the color object.
#     r = a.rgb.r
#     g = a.rgb.g
#     b = a.rgb.b
#     final_color = (r, g, b)
#     rgb_colors.append(final_color)
# print(rgb_colors)
import random
import turtle
from turtle import Screen
from turtle import Turtle
list_colors = [(1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]
tal = Turtle()
turtle.colormode(255)

tal.setheading(225) #Points the direction to 225
tal.penup()
tal.forward(250) #Move the turtle by 250 points so it starts from the right spot
tal.setheading(0) #Set heading to 0 si that it makes a straight line.
tal.pendown()
tal.hideturtle()
tal.speed(0)

dots = 100
def line():
    for dots_drawn in range(1, dots+1):
        current_color = random.choice(list_colors)
        tal.dot(20, current_color)
        tal.penup()
        tal.forward(50)
        tal.pendown()

        if dots_drawn % 10 == 0:
            tal.left(90)
            tal.penup()
            tal.forward(50)
            tal.left(90)
            tal.forward(500)
            tal.setheading(0)
            tal.pendown()



line()








screen = turtle.Screen()
screen.exitonclick()
