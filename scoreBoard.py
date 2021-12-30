from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"{self.player2_score}      {self.player1_score}", align="center", font=("Courier", 32, "bold"))

    def increment_score_1(self):
        self.player1_score += 1
        self.clear()
        self.update_score_board()

    def increment_score_2(self):
        self.player2_score += 1
        self.clear()
        self.update_score_board()
