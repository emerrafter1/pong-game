from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10




    def move(self):
        new_y_cor = self.ycor() + self.y_move
        new_x_cor = self.xcor() + self.x_move
        self.goto(new_x_cor, new_y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.y_move *= -1
        self.x_move *= -1
