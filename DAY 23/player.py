from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.refresh()

    def move(self):
        if self.ycor() != FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def refresh(self):
        self.goto(STARTING_POSITION)














