from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

X_EDGE = 400


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)

    def up(self):
        if self.paddle.ycor() + MOVE_DISTANCE < 260:
            new_y = self.paddle.ycor() + 20
            self.paddle.goto(self.paddle.xcor(), new_y)
        elif self.paddle.ycor() + MOVE_DISTANCE == 260:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor())

    def down(self):
        if self.paddle.ycor() - MOVE_DISTANCE > -250:
            new_y = self.paddle.ycor() - 20
            self.paddle.goto(self.paddle.xcor(), new_y)
        elif self.paddle.ycor() - MOVE_DISTANCE == -250:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor())
