from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

tim.speed(0)
tim.pensize(5)
colors = ['red', 'blue', 'yellow', 'green', 'cyan', 'purple']


proceed = True
while proceed:
    move_choice = random.randint(20, 40)
    right_left = random.randint(1, 2)
    if right_left == 1:
        tim.color(random.choice(colors))
        tim.forward(move_choice)
        tim.right(90)
    elif right_left == 2:
        tim.color(random.choice(colors))
        tim.forward(move_choice)
        tim.left(90)

screen = Screen()
screen.exitonclick()
