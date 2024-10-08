from turtle import Turtle, Screen
tal = Turtle()
screen = Screen()


screen.listen() # This allows the turtle screen to listen to the commands.


def forward():
    tal.forward(20)
def back():
    tal.back(20)
def left():
    tal.left(10)
def right():
    tal.right(10)
def clear_screen():
    tal.clear()
    tal.penup()
    tal.home()
    tal.pendown()

screen.onkey(forward, "w")
screen.onkey(back, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
