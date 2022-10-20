from turtle import Turtle
paddles =[]


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)
        self.left(90)
        self.speed("fastest")
        self.showturtle()


    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)

