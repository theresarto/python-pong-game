from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle(-360, 0)
right_paddle = Paddle(350, 0)
ball = Ball()

screen.listen()
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")


def dashed_line():
    dash = Turtle()
    dash.color("white")
    dash.ht()
    dash.width(5)
    dash.penup()
    dash.setheading(270)
    dash.goto(0, 300)
    dash.speed("fastest")

    for i in range(30):
        dash.pendown()
        dash.forward(10)
        dash.penup()
        dash.forward(20)


dashed_line()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if abs(ball.ycor()) >= 280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 300:
        print("made contact")
        # ball.bounce_x()

        screen.exitonclick()
