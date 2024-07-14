from turtle import Turtle
from random import randrange, randint

HEADING = randrange(40, 360, 90)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("orange")
        self.setheading(HEADING)
        self.move_speed = 0.1

    def move(self):
        self.forward(10)
        if abs(self.ycor()) >= 280:
            new_heading = self.heading() * -1
            self.setheading(new_heading)

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def edge_of_screen(self):
        return abs(self.xcor()) >= 400

    def reset_position(self):
        self.goto(0,0)
        new_heading = randrange(40, 360, 30)
        self.setheading(new_heading)
        self.move_speed = 0.1
        self.move()
