import turtle

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas
states = pandas.read_csv("50_states.csv")
allstates = states.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="What's another state name?").title()
    if answer_state in allstates:
        guessed_states.append(answer_state)
        current_state = states[states.state == answer_state]
        x_cor = current_state.x.item() #.item() - accesses the item excluding the index value.
        y_cor = current_state.y.item()
        tal = turtle.Turtle()
        tal.hideturtle()
        tal.penup()
        tal.goto(x_cor, y_cor)
        tal.write(answer_state, font=('arial', 8, 'normal'))
    if answer_state.lower() == "exit":
        missing_states = []
        for states in allstates:
            if states not in guessed_states:
                missing_states.append(states)
        data = pandas.DataFrame(missing_states)
        data.to_csv("States_to_learn.csv")
        break


# def get_mouse_click_coor(x, y): This could be used to get the x and y coordinates of each state by clicking on them.
# x and y coordinates are already stored in the csv file.
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor) #Event listener-when the mouse clicks.


