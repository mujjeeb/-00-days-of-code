from turtle import Turtle



colour = ['red', 'yellow', 'green', 'blue', 'orange', 'purple', 'brown']


class Obstacles:
    def __init__(self):
        self.all_obstacles = []
        self.y_value = 0
        self.colour = "yellow"
        self.create_obstacles()

    def create_obstacles(self):
        for n in range(7):
            for i in range(7):
                new_obstacle = Turtle("square")
                new_obstacle.shapesize(stretch_wid=1.2, stretch_len=5)
                new_obstacle.penup()
                new_obstacle.setpos(-330, self.y_value)
                new_obstacle.penup()
                new_obstacle.color(colour[n])
                new_obstacle.forward(i * 110)
                self.all_obstacles.append(new_obstacle)
            self.y_value += 40
