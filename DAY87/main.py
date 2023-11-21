import time
from turtle import Screen, Turtle
from paddle import Paddle
from obstacles import Obstacles
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

# Initializing the paddle
paddle = Paddle((0, -250))

# Initializing the obstacles
obstacles = Obstacles()

# Initializing the ball
ball = Ball()

# Initializing Scoreboard
scoreboard = Scoreboard()

# Listening for the right and left key to move the paddle
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    # time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -280:
        game_is_on = False

    # Detect collision with paddle
    if ball.distance(paddle) < 80 and ball.ycor() < -250:
        ball.bounce_y()

    # Detect collision with obstacles
    for obstacle in obstacles.all_obstacles:
        if ball.distance(obstacle) < 50 and ball.ycor() > -5:
            ball.bounce_y()
            obstacles.all_obstacles.remove(obstacle)
            obstacle.hideturtle()
            scoreboard.add_point()


        if not obstacles.all_obstacles:
            game_is_on = False

screen.exitonclick()
