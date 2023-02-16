import turtle as t
from turtle import Screen
from random_color import RandomTuple


tim = t.Turtle()

# print(rand_color)
# tim.color(rand_color)
# tim.speed(1)
# tim.pen(speed=1)

rand_color = RandomTuple().random_tuple()
tim.color(rand_color)
tim.speed('fastest')
tim.circle(100)
current_heading = tim.heading()

# for _ in range(2, 90):
#     rand_color = RandomTuple().random_tuple()
#     # print(_)
#     # print(rand_color)
#     tim.color(rand_color)
#     tim.circle(100)
#     tim.left(_)
#     print(tim)


screen = Screen()
screen.exitonclick()