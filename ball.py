from turtle import Turtle
from random import randrange

HEADING = randrange(40, 360, 30)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("orange")
        self.setheading(HEADING)

    def move(self):
        self.forward(20)
        if abs(self.ycor()) >= 280:
            new_heading = self.heading() * -1
            self.setheading(new_heading)

    def bounce_paddle(self):
        self.setheading(180 - self.heading())

    def edge_of_screen(self):
        return abs(self.xcor()) >= 400
