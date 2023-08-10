from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

color_list = [("red"),("orange"),("yellow"),("green"),("blue"),("indigo"),("violet"),("yellow")]

timmy.penup()
timmy.goto(-310,-290)
timmy.setheading(0)

max_dots = 196
for N in range(1,max_dots):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
        
        
        if N % 15 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(750)
            timmy.setheading(0)
    
        

timmy.hideturtle()
screen = Screen()
screen.exitonclick()

