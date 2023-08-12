from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    # Detect collision with right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect collision with left wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

screen.exitonclick()
