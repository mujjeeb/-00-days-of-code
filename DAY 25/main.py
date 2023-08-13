import turtle

import pandas

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S State game")
image = "blank_states_img_gif"

screen.addshape("blank_states_img.gif")
# screen.bgpic("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
turtle = turtle.Turtle()
data = pandas.read_csv("50_states.csv")
name_of_states = data.state
is_game_on = True
score = 0
while is_game_on:

    answer_state = screen.textinput(title=f"{score} / 50 correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    name_of_states_list = name_of_states.tolist()

    for st in name_of_states_list:

        if answer_state == st:
            state_x = float(data[data['state'] == answer_state].x)
            state_y = float(data[data['state'] == answer_state].y)
            turtle.penup()
            turtle.goto(state_x, state_y)
            turtle.write(answer_state, align="right")
            turtle.hideturtle()
            score += 1
            name_of_states_list.remove(answer_state)

screen.exitonclick()
