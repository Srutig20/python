import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSlateBlue")
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")


for _ in range(500):
    timmy.color( random_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
