from turtle import Turtle

class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("grey")
        self.ht()
        self.width(5)
        self.penup()
        self.setheading(270)
        self.goto(0, 300)
        self.speed("fastest")
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
