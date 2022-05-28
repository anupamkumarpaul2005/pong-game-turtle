from turtle import Turtle


def create_border():
    border = Turtle()
    border.width(10)
    border.color("white")
    border.penup()
    border.hideturtle()
    border.goto(0, -300)
    border.seth(90)
    while border.ycor() < 300:
        border.pendown()
        border.fd(10)
        border.penup()
        border.fd(20)


class Scoreboard:
    def __init__(self, position):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(position)
        self.show_score()

    def show_score(self):
        self.scoreboard.write(self.score, align="center", font=("Courier", 80, "normal"))

    def change_score(self):
        self.score += 1
        self.scoreboard.clear()
        self.show_score()
