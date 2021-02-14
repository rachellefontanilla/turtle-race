from turtle import Turtle, Screen
import random

is_race_on = False

""" Set up """
screen = Screen()
screen.setup(width=500, height=400)
screen.tracer(0)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="           Which turtle will win the race?\n (red, orange, yellow, green, blue, purple) \n                        Enter a colour: ",
)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

""" Create Turtles """
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    screen.update()
    all_turtles.append(new_turtle)

result = Turtle()
result.hideturtle()
result.penup()

""" Start Race """
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        screen.update()
        if turtle.xcor() >= 230:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                result.write(
                    f"         Yay! You won!\nThe {winning_colour} turtle is the winner!",
                    align="center",
                    font=("Courier", 15, "normal"),
                )
            else:
                result.write(
                    f"        Sorry, you lost.\nThe {winning_colour} turtle is the winner!",
                    align="center",
                    font=("Courier", 15, "normal"),
                )
            result.color("black")
            is_race_on = False

screen.exitonclick()