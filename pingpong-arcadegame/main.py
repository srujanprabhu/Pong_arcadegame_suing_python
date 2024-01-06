from turtle import Turtle, Screen
from paddel import Paddel
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
score = Scoreboard()
paddel_r = Paddel((350,0))
paddel_l = Paddel((-350,0))
ball = Ball()


screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

#creating a padd

screen.listen()
screen.onkeypress(paddel_r.go_up,"Up")
screen.onkeypress(paddel_r.go_down,"Down")
screen.onkeypress(paddel_l.go_up,"w")
screen.onkeypress(paddel_l.go_down,"s")

game_is_on = True





while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collisions with wall
    if ball.ycor() > 300 or ball.ycor() <-300:
        #bounce
        ball.bounce_y()


    #detect collisiow with  paddel
    if ball.distance(paddel_r) < 50 and ball.xcor() > 340 or ball.distance(paddel_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()





screen.exitonclick()
