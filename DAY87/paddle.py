from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1.2, stretch_len=10)
        self.penup()
        self.goto(position)

    def go_right(self):
        self.forward(20)

    def go_left(self):
        self.forward(-20)
