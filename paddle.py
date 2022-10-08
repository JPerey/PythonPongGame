from turtle import Turtle

PADDLE_MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=10)
        self.goto(-350, 0)
        self.y_height = 0

    def second_paddle(self):
        self.setpos(350, 0)

    def move_up(self):
        self.y_height += PADDLE_MOVE_DISTANCE
        self.goto(-350, self.y_height)

    def move_down(self):
        self.y_height -= PADDLE_MOVE_DISTANCE
        self.goto(-350, self.y_height)

    def move_up2(self):
        self.y_height += PADDLE_MOVE_DISTANCE
        self.goto(350, self.y_height)

    def move_down2(self):
        self.y_height -= PADDLE_MOVE_DISTANCE
        self.goto(350, self.y_height)
