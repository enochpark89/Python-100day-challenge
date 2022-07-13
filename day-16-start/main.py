# Use a Turtle class to create a turtle object.

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.shapesize(15)
#
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

# How do you create a table?
# Package used: prettyTable

import prettytable
# Right Go to -> view source code

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pickachu","Squirtle", "Charmander"])

table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)