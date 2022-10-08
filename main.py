from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Python Pong")
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle()
paddle2.second_paddle()
ball = Ball()
ball.initial_move()

game_over = False
screen.listen()
screen.update()

screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")

screen.onkey(paddle2.move_up2, "Up")
screen.onkey(paddle2.move_down2, "Down")

while not game_over:
    ball.move_ball()
    screen.update()
    time.sleep(.1)




























screen.exitonclick()
