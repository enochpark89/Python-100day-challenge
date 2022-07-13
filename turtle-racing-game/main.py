
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

# Screen setup
screen.setup(width=500, height=400)

# Pop-up to the user and to enter the text.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# color of rainbow in a list
colors = ["red", "orange", "yellow", "green", "blue", "purple", ]
turtles = []

# Make a list of Turtle objects.

# Coordinate of a first turtle.
x_value = -230
y_value = -100
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=x_value, y=y_value)
    y_value += 30
    turtles.append(tim)

# Make the turtle move forward by random amount
if user_bet:
    is_race_on = True

while is_race_on:

    # Iterate each turtle and move random distance
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on= False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Detect the finishline

screen.exitonclick()
