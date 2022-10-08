from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.degrees(360)
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move = -self.y_move

    def paddle_bounce(self):
        self.x_move = -self.x_move
