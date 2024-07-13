from turtle import Turtle

TO_LEFT = 135
TO_RIGHT = 45
Y_EDGE = 250

class Ball:
    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.penup()
        self.ball.color("orange")
        self.ball.speed("fastest")
        self.ball.goto(0,0)

    def move(self):
        self.ball.setheading(TO_LEFT)
        self.ball.forward(20)

    def edge_of_screen(self):
        if self.ball.ycor() + 10 == Y_EDGE:
            if self.ball.setheading(TO_LEFT):
                self.ball.setheading(-TO_LEFT)
                self.ball.forward(20)
            elif self.ball.setheading(TO_RIGHT):
                self.ball.setheading(-TO_RIGHT)
                self.ball.forward(20)

        elif self.ball.ycor() + 10 == -Y_EDGE:
            if self.ball.setheading(-TO_LEFT):
                self.ball.setheading(TO_LEFT)
                self.ball.forward(20)
            elif self.ball.setheading(-TO_RIGHT):
                self.ball.setheading(-TO_RIGHT)
                self.ball.forward(20)

