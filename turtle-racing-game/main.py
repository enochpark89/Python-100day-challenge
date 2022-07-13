from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Move a turtle forward by 10.
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    tim.right(5)

def move_counter_clockwise():
    tim.left(5)

def clear_screen():
    screen.resetscreen()

screen.listen()
# Use an event listener


# Functions as Inputs
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()

# Create a turtle to move in multipile direction
