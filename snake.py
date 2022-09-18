import turtle
from turtle import Turtle

class Snake(Turtle):

    X_Y = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180


    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for coord in self.X_Y:
            self.add_segment(coord)

    def add_segment(self, coord):
        body = Turtle()
        body.penup()
        body.shape("square")
        body.color("white")
        body.goto(coord)
        self.segments.append(body)

    def grow(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range((len(self.segments)-1), 0,-1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newx, newy)

        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)
