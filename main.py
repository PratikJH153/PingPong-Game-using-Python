from turtle import Screen
from paddle import Paddle
from scoreBoard import ScoreBoard
from ball import Ball
from drawLine import DrawLine
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")

screen.tracer(0)


player1 = Paddle(410)
player2 = Paddle(-410)
ball = Ball()
scoreBoard = ScoreBoard()
DrawLine()

screen.listen()

screen.onkeypress(key="Up", fun=player1.up)
screen.onkeypress(key="Down", fun=player1.down)
screen.onkeypress(key="w", fun=player2.up)
screen.onkeypress(key="s", fun=player2.down)

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect ball collision with wall
    if abs(ball.ycor()) >= 290:
        ball.bounce_y()

    # Detect ball collision with paddle
    if (ball.distance(player1) <= 50 or ball.distance(player2) <= 50) and abs(ball.xcor()) > 380:
        ball.bounce_x()

    # Detect ball misses right paddle
    if ball.xcor() > 430:
        ball.reset_position()
        scoreBoard.increment_score_2()

    # Detect ball misses left paddle
    if ball.xcor() < -430:
        ball.reset_position()
        scoreBoard.increment_score_1()

screen.exitonclick()
