from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

X_EDGE = 400


class Paddle(Turtle, x_edge, y_center):

    def __init__(self):
        self.paddle = Turtle()
        self.shape("square")
        self.color("white", "white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.x_edge =  x_edge
        self.y_center = y_center
        self.goto(self.x_edge, self.y_center)
        self.forward(MOVE_DISTANCE)

    # def move(self):
    #     self.paddle.forward(MOVE_DISTANCE)

    def up(self):
        if self.paddle.ycor() + 25 + MOVE_DISTANCE <= Y_EDGE:
            self.paddle.setheading(UP)
            self.move()

    def down(self):
        if self.paddle.ycor() - 25 - MOVE_DISTANCE >= -Y_EDGE:
            self.paddle.setheading(DOWN)
            self.move()
