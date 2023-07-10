import random
from turtle import Turtle, Screen

def reset_turtles():
    turtles = []

    for turtle_index in range(0, 6):
        tim = Turtle(shape="turtle")
        tim.penup()
        tim.color(colors[turtle_index])
        tim.goto(x=-230, y=y_positions[turtle_index])
        turtles.append(tim)
    return turtles

def random_turtle_move(turtles):
    winning_turtle = None
    while not winning_turtle:
        for single_turtle in turtles:
            single_turtle.forward(random.choice(random_moves))
            if single_turtle.xcor() > 230:
                print(f"The {single_turtle.pencolor()} won!")
                winning_turtle = single_turtle.pencolor()
                break
    return winning_turtle

def who_won(user_bet, winning_turtle):
    if user_bet.lower() == winning_turtle:
        print("Well done you won")
    else:
        print("You lost")

def play_again():
    to_play_again = screen.textinput("Play Again", "Do you want to play again. Please enter y or n:")
    if to_play_again.lower() == "y":
        return False
    else:
        print("Goodbye")
        return True

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
random_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

game_over = False
while not game_over:
    user_bet = screen.textinput(title="The Turtle Race!", prompt="Which turtle will win the race? Enter a color: ")
    turtles = reset_turtles()
    winning_turtle = random_turtle_move(turtles)
    who_won(user_bet, winning_turtle)
    game_over = play_again()

screen.exitonclick()
