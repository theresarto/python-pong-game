from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from centerline import CenterLine

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle(-360, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
centerline = CenterLine()

screen.listen()
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.distance(left_paddle) < 30 and abs(ball.xcor()) >= 335 \
            or ball.distance(right_paddle) < 40 and abs(ball.xcor()) >= 325:
        ball.bounce_paddle()
    if ball.edge_of_screen():
        game_is_on = False
        print("Game Over")

screen.exitonclick()
