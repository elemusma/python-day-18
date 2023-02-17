import turtle as t
from turtle import Screen
from random_color import RandomTuple


tim = t.Turtle()

# print(rand_color)
# tim.color(rand_color)
# tim.speed(1)
# tim.pen(speed=1)

i = 0
# for _ in range(5):
def draw_spirograph(size_of_graph):

    for _ in range(int(360 / size_of_graph)):
        rand_color = RandomTuple().random_tuple()
        tim.color(rand_color)
        tim.speed('fastest')
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_graph)
        print(size_of_graph)

draw_spirograph(10)


    # while i < 360:
    #     i += 1
    #     print(i)
    #     rand_color = RandomTuple().random_tuple()
    #     tim.color(rand_color)
    #     tim.speed('fastest')
    #     tim.circle(100)
    #     current_heading = tim.heading()
    #     tim.setheading(i)
    #     print(current_heading)

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