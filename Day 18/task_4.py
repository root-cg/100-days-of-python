import turtle as t
import random
import colorgram


tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


rgb_colors = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), 
 (243,34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]

# colors = colorgram.extract("100-days-of-python\Day 18\images.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_choice = (r, g, b)
#     rgb_colors.append(color_choice)

# print(rgb_colors)
