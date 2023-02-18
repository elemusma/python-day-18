import turtle as t
from turtle import Screen
from random_color import RandomTuple

tim = t.Turtle()
# t.screensize(canvwidth=5000, canvheight=500,bg="white")

def make_columns(num_of_cols):

    # tim.penup()
    # tim.setx(-50)
    for _ in range(num_of_cols):
        # print(tim.xcor())
        # print(tim.pos())
        rand_color = RandomTuple().random_tuple()
        tim.color(rand_color)
        tim.speed('fastest')
        tim.pendown()
        tim.dot(20, rand_color)
        tim.penup()
        tim.forward(50)
        
        # tim.setx(0)
        # tim.sety(tim.ycor() + 50)

# make_columns(10)

def make_rows(num_of_rows):

    start_y = tim.ycor()
    for _ in range(num_of_rows):
        make_columns(num_of_rows)
        start_y += 50
        tim.sety(start_y)
        # print(start_y)
        # print(tim.xcor())
        tim.setx(0)
        tim.penup()


make_rows(5)



# circles 20 in size
# 50 steps apart
# 10x10

def moves_rows():
    pass


screen = Screen()

print(screen.window_width())
print(screen.window_height())

screen.exitonclick()