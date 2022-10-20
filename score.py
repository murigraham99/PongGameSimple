from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.ht()
        self.score_p1 = 0
        self.score_p2 = 0
        self.update()

    def update (self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.score_p1, False, align="center", font=("Arial", 30, "bold"))
        self.goto(x=100, y=200)
        self.write(self.score_p2, False, align="center", font=("Arial", 30, "bold"))

    def p1_point(self):
        self.score_p1 +=1
        self.update()

    def p2_point(self):
        self.score_p2 +=1
        self.update()