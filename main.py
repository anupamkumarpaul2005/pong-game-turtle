from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, create_border

s = Screen()
s.setup(width=800, height=700)
s.bgcolor("black")
s.tracer(0)
s.title("Pong Game")
game = True

ball = Ball()
p1 = Paddle("left")
p2 = Paddle("right")
l_score = Scoreboard((-60, 250))
r_score = Scoreboard((60, 250))
create_border()
s.update()

s.listen()
s.onkeypress(p2.move_up, "Up")
s.onkeypress(p2.move_down, "Down")
s.onkeypress(p1.move_up, "w")
s.onkeypress(p1.move_down, "s")

while game:
    s.update()
    ball.hit_wall()
    ball.move()
    ball.hit_paddle(p1, p2)
    if ball.out_of_bounds(l_score, r_score):
        ball.reset_game()

s.exitonclick()
