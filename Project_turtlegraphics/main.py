from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.color("maroon")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
# '''for _ in range(3):
#     timmy.right(120)
#     timmy.forward(100)
# for _ in range(4):
#     timmy.color("blue")
#     timmy.right(90)
#     timmy.forward(100)'''

colours = ["blue", "orange", "maroon", "magenta", "black", "grey","green", "olive"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range (3,11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)

















screen= Screen()
screen.exitonclick()

