# import turtle as t
# from turtle import Screen
import colorgram

# tim = t.Turtle()

colors = colorgram.extract('hirst-spot-painting.jpg', 100)
color_list = []


for color in colors:
    # print(count)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)
    # rgb = colors[count]
    # color = rgb.rgb
    # color_list.append(color)

print(color_list)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s

# print(rgb)

# screen = Screen()
# screen.exitonclick()