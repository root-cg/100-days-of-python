from turtle import Turtle, Screen


bill = Turtle()
bill.shape("turtle")
bill.color("green")



# for _ in range(15):
#     bill.forward(10)
#     bill.penup()
#     bill.forward(10)
#     bill.pendown()


def optimized(angle, sides):
    for side in range(sides):
        bill.forward(100)
        bill.right(angle)


optimized(120, 3)
optimized(90, 4)
optimized(72, 5)
optimized(60, 6)
optimized(52, 7)
optimized(45, 8)


screen_wait = Screen()
screen_wait.exitonclick()
