from turtle import Turtle, Screen
from scoreboard import Score_board
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
my_turtle = Turtle()


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

scoreboard = Score_board()

ball = Ball()


game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()



    #Detect collision with paddle 
    #collision for both paddles 

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()


    #paddle miss the ball
    # right paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.increase_score_l()
    
    #left paddle
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.increase_score_r()



screen.exitonclick()