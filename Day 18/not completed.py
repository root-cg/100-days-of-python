import turtle as t
import random

t.colormode(255)

rgb_colors = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), 
 (243,34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]


bill = t.Turtle()


for dot in range(10):
    
    bill.dot(20, random.choice(rgb_colors))
    bill.penup()
    bill.forward(50)

screen = t.Screen()

screen.exitonclick()