from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 600)
screen.title("Pong Game")
score= Score()



p1= Paddle((350,0))
p2 = Paddle((-350,0))
ball= Ball()




screen.listen()

screen.onkey(p1.move_up,"Up")
screen.onkey(p1.move_down, "Down")
screen.onkey(p2.move_up,"w")
screen.onkey(p2.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.b_speed)
    screen.update()
    ball.move()
    #collision with wall
    if ball.ycor()>295 or ball.ycor() < -295:
        ball.bounce_y()

    #collision with paddle1

    if ball.distance(p1) < 50 and ball.xcor()> 320 or ball.distance(p2)<50 and ball.xcor() < -320:
        print("contact")
        ball.bounce_x()

    #out of bounds p1

    if ball.xcor() > 380:
        turtle = Turtle
        ball.reset_pos()
        score.p1_point()

    #out of bounds p2

    if ball.xcor()< -380:
        turtle = Turtle
        ball.reset_pos()
        score.p2_point()





screen.exitonclick()
