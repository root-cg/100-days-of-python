# import my_module
# import turtle


# check = my_module.another_variable

# chill = turtle.Turtle()

# chill.shape("turtle")
# chill.forward(100)
# chill.color("chocolate4")

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Pokemon Type", ["Electric","Water", "Fire"])
table.align = "l"

print(table)