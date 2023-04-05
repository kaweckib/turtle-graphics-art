from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

colors = ['red', 'blue', 'yellow', 'green', 'cyan', 'purple']


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def draw_shape_left(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.left(angle)


for shape_side_n in range(3, 13):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

for shape_side_l in range(3, 13):
    tim.color(random.choice(colors))
    draw_shape_left(shape_side_l)


screen = Screen()
screen.exitonclick()
