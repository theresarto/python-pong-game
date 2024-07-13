from turtle import Screen, Turtle
from paddle import Paddle

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.update()
time.sleep(0.1)

left_paddle = Paddle(-360, 0)
right_paddle = Paddle(360, 0)

screen.listen()
screen.onkey(fun=left_paddle.up, key="Up")
screen.onkey(fun=left_paddle.down, key="Down")


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
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
