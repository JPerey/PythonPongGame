from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.update()

screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")

screen.onkey(paddle2.move_up2, "Up")
screen.onkey(paddle2.move_down2, "Down")


def game_run():
    game_over = False
    p1_score = 0
    p2_score = 0

    while not game_over:
        ball.move_ball()
        screen.update()
        time.sleep(.1)
        scoreboard.print_score(p1_score, p2_score)

        print(f"distance ball from paddle2: {ball.distance(paddle2)}")

        if ball.distance(ball.xcor(), y=295) < 10 or ball.distance(ball.xcor(), y=-285) < 10:
            ball.bounce()

        if ball.distance(paddle1) < 15 or ball.distance(paddle2) < 15:
            ball.paddle_bounce()


game_run()

screen.exitonclick()
