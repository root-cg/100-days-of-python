import turtle as t
import random
import colorgram

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

directions = [0, 90, 180, 270]
t.pensize(15)
t.speed(0)


for _ in range(1000):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(directions))



screen = t.Screen()

screen.exitonclick()

