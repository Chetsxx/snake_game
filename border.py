from turtle import Turtle
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("yellow")
        self.penup()
        self.goto(280, 280)
        self.pendown()
        self.setheading(270)
        self.forward(560)
        self.setheading(180)
        self.forward(560)
        self.setheading(90)
        self.forward(560)
        self.setheading(0)
        self.forward(560)
