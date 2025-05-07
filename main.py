from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
scoreboard = Scoreboard()



while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detech collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detech collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()




    #Detech ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()




    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()








screen.exitonclick()