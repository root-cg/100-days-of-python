from turtle import Turtle, Screen
from random import randint

screen = Screen()


screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="which turtule will win the race Enter a color: ")
colors_a = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtle =[]

value = 0
for i in range(len(colors_a)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors_a[i])  
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-(100 - value))
    value += 50
    all_turtle.append(new_turtle)

is_race = False

if user_bet:
    is_race = True


while is_race:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race =False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        rand_distance=randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
