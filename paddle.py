
from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed("slowest")



    def up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
