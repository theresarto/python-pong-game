from turtle import Screen
from paddle import Paddle
from ball import Ball
from centerline import CenterLine
from scoreboard import ScoreBoard, Score

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
scoreboard = ScoreBoard()
left_score = Score(-70, 195)
right_score = Score(70, 190)

screen.listen()
screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.distance(left_paddle) < 63 and abs(ball.xcor()) >= 335 \
            or ball.distance(right_paddle) < 63 and abs(ball.xcor()) >= 325:
        ball.bounce_paddle()
    if ball.edge_of_screen():
        if ball.xcor() <= -380:
            ball.reset_position()
            right_score.score += 1
            right_score.update_score()
        elif ball.xcor() >= 380:
            ball.reset_position()
            left_score.score += 1
            left_score.update_score()
screen.exitonclick()
