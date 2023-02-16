from turtle import Turtle, Screen
from attributes import colors
import random

tim = Turtle()

# for i in range(20):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_in in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_in)

# starting_side = 3
# angle = 360
# start = 0
# while starting_side < 11:
#     random_color = colors[start]
#     for i in range(starting_side):
#         tim.color(random_color)
#         tim.forward(100)
#         tim.right(angle/starting_side)

#     starting_side += 1
#     start += 1
    # print(starting_side)


screen = Screen()
screen.exitonclick()