from turtle import Turtle
import time
from random import choice


class Ball:
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.speed("fastest")
        self.velocity_x = 0.1
        self.velocity_y = 0.1
        self.number_of_hits = 0

    def move(self):
        self.ball.goto(self.ball.xcor() + self.velocity_x, self.ball.ycor() + self.velocity_y)

    def hit_paddle(self, p1, p2):
        for i in range(5):
            if self.ball.distance(p1.paddle[i]) < 20 or self.ball.distance(p2.paddle[i]) < 20:
                self.velocity_x *= -1
                self.increase_speed()
                return

    def increase_speed(self):
        self.velocity_y = (self.velocity_y / abs(self.velocity_y)) * (abs(self.velocity_y) + 0.01)
        self.velocity_x = (self.velocity_x / abs(self.velocity_x)) * (abs(self.velocity_x) + 0.01)

    def hit_wall(self):
        y = self.ball.ycor()
        if y > 290 or y < -290:
            self.velocity_y *= -1

    def out_of_bounds(self, left, right):
        x = self.ball.xcor()
        if x < -390:
            right.change_score()
            return True
        elif x > 390:
            left.change_score()
            return True
        return False

    def reset_game(self):
        self.number_of_hits = 0
        time.sleep(1)
        self.velocity_x *= choice([1, -1])
        self.velocity_y *= choice([1, -1])
        self.ball.home()
