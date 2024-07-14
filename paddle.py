from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.paddle = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def up(self):
        if self.ycor() + MOVE_DISTANCE < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        elif self.ycor() + MOVE_DISTANCE == 260:
            self.goto(self.xcor(), self.ycor())

    def down(self):
        if self.ycor() - MOVE_DISTANCE > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        elif self.ycor() - MOVE_DISTANCE == -250:
            self.goto(self.xcor(), self.ycor())
