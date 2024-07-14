from turtle import Turtle

ALIGN = "center"
LARGE_FONT = ("Courier", 60, "bold")
REG_FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.goto(0, 260)
        self.color("white")
        self.speed("fastest")
        self.write("SCORE", align=ALIGN, font=REG_FONT)
        self.goto(0, 200)
        self.write("-", align=ALIGN, font=LARGE_FONT)


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.speed("fastest")
        self.goto(x, y)
        self.update_scoreboard()


    def update_score(self):
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGN, font=LARGE_FONT)
