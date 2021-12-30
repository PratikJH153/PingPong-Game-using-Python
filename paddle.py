from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(x_position, 0)

    def up(self):
        if self.ycor() < 240:
            previous_y = self.ycor()
            self.sety(previous_y + 20)

    def down(self):
        if self.ycor() > -240:
            previous_y = self.ycor()
            self.sety(previous_y - 20)
