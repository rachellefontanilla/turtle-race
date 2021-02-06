from turtle import Turtle, Screen
import random

is_race_on = False

""" Set up """
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a colour: "
)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

""" Create Turtles """
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.setpos(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

""" Start Race """
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"Yay! You won! The {winning_colour} turtle is the winner!")
            else:
                print(f"Sorry, you lost. The {winning_colour} turtle is the winner!")
            is_race_on = False

screen.exitonclick()