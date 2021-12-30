from turtle import Turtle


class DrawLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.draw_line()

    def draw_line(self):
        self.penup()
        self.pensize(3)
        self.pencolor("white")
        self.goto(0, 290)
        self.right(90)
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)