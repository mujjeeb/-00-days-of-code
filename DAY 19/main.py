from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.listen()
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "purple"]
y_cod = -90
all_turtles = []
for color_in_rainbow in colors:
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color_in_rainbow)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cod)
    all_turtles.append(new_turtle)
    y_cod += 50

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won!, {winning_color.title()} won!")
            else:
                print(f"You lost!, {winning_color.title()} won!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
