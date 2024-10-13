from turtle import Turtle
STARTING_POSITIONS =  [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
        def __init__(self):
            self.squareblocks = []
            self.create_snake() #Whenever we create an object from Snake it will create 3 objects (snake blocks) using the starting positions
            self.head = self.squareblocks[0] #Represents the first block of snake.

        def create_snake(self):
            for new in STARTING_POSITIONS:
                self.add_block(new) #The add_block functions take position, we are here looping through first 3 positions of the snake.
                # Older function, later modified using add_block because new block has to be created.
                # block = Turtle("square")
                # block.color("white")
                # block.penup()
                # block.goto(new)
                # self.squareblocks.append(block)

        def add_block(self, position):
            block = Turtle("square")
            block.color("white")
            block.penup()
            block.goto(position)
            self.squareblocks.append(block)

        def after_food(self):
            self.add_block(self.squareblocks[-1].position()) #Using the position method from turtle class.
            #Squareblocks[-1] gets hold of last square block added and then new block goes to.


        def move(self):
            for block_num in range(len(self.squareblocks) - 1, 0, -1):  # (start = 2, stop = 0, step = -1)
                # Start is written as len so that if there are 10 squares  it gets hold of the last one. Indices are -1 than actual length.
                # The below thing will first happen for the last one and then for the second last as range goes from 2,1,0.
                new_x = self.squareblocks[block_num - 1].xcor()  # Gets hold of the 2nd or the one front square and store its xcor value.
                new_y = self.squareblocks[block_num - 1].ycor()  # Similarly for the ycor.
                self.squareblocks[block_num].goto(new_x, new_y)  # Setting position of the last square to the second last square.
            self.head.forward(MOVE_DISTANCE)

        def up(self):
            if self.head.heading() != DOWN: #This checks if the first head of the snake's current heading is equal to down or no.
                self.head.setheading(UP)
        def down(self):
            if self.head.heading() != UP:
                self.head.setheading(DOWN)
        def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)
        def left(self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)
