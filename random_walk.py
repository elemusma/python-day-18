# from turtle import Turtle, Screen
import turtle as t
from turtle import Screen
from attributes import colors, steps, speed
import random

tim = t.Turtle()
t.colormode(255)

def random_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generated_tuple = (r, g, b)
    return generated_tuple

def random_walk(steps, color, line_width, direction, speed):
    tim.pensize(line_width)
    tim.forward(steps)
    tim.right(direction)
    tim.color(color)
    tim.speed(speed)

# def random_steps(steps_param):
#     tim.forward(steps_param)


# def random_color(color_param):
#     tim.color(color_param)


# def random_width(width_param):
#     tim.pensize(width_param)


# def random_direction(direction_param):
#     tim.right(direction_param)


# def random_speed(speed_param):
#     tim.speed(speed_param)


i = 0
while i < 20:
    # random_steps(random.choice(steps)*5)
    # random_direction(random.randrange(0, 360, 90))
    # random_width(random.randint(1, 10))
    # random_color(random.choice(colors))
    # random_speed(random.choice(speed))
    rand_color = random_tuple()
    random_walk((random.choice(steps)*10), rand_color, random.randint(1, 10), random.randrange(0, 360, 90), random.choice(speed))
    # random_walk((random.choice(steps)*10), random.choice(colors), random.randint(1, 10), random.randrange(0, 360, 90), random.choice(speed))
    print(i)
    i += 1


screen = Screen()
screen.exitonclick()

