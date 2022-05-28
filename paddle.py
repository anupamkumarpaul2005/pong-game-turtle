from turtle import Turtle

DISTANCE = 20


class Paddle:
    def __init__(self, side="left"):
        self.paddle = []
        if side == "left":
            self.x = -380
        elif side == "right":
            self.x = 380
        self.y = 40
        for _ in range(5):
            self.create_paddle()

    def create_paddle(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.speed("fastest")
        segment.goto(self.x, self.y)
        self.y -= 20
        self.paddle.append(segment)

    def move_up(self):
        head = self.paddle[0]
        if head.ycor() > 280:
            return
        head.seth(90)
        for i in range(len(self.paddle) - 1, 0, -1):
            self.paddle[i].setpos(self.paddle[i - 1].pos())
        head.fd(DISTANCE)

    def move_down(self):
        head = self.paddle[len(self.paddle) - 1]
        if head.ycor() < -280:
            return
        head.seth(270)
        for i in range(len(self.paddle) - 1):
            self.paddle[i].setpos(self.paddle[i + 1].pos())
        head.fd(DISTANCE)
