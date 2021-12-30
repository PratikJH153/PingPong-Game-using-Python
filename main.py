from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")

screen.tracer(0)

player1 = Paddle(410)
player2 = Paddle(-410)

screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    screen.onkeypress(key="Up", fun=player1.up)
    screen.onkeypress(key="Down", fun=player1.down)

screen.exitonclick()
