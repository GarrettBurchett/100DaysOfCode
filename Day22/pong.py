from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    # Detect when R paddle misses
    if ball.xcor() >= 380:
        scoreboard.l_point()
        ball.reset_position()
        r_paddle.reset((350, 0))
        l_paddle.reset((-350, 0))
        time.sleep(1)

    # Detect when L paddle misses
    if ball.xcor() <= -380:
        scoreboard.r_point()
        ball.reset_position()
        r_paddle.reset((350, 0))
        l_paddle.reset((-350, 0))
        time.sleep(1)


screen.exitonclick()