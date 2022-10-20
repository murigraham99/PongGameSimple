from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.b_speed = 0.03
        self.x = 0


    def move(self):
        self.penup()
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    def bounce_y(self):
        self.y_move *= -1
        self.b_speed *= 0.9

    def bounce_x(self):
            self.x_move *= -1
            self.b_speed *= 0.9

    def reset_pos(self):
        self.speed("slowest")
        self.goto(0,0)
        self.bounce_x()







