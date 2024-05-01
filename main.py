import turtle
import pandas

TOTAL_STATES = 50

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

text = turtle.Turtle()

# Reading data from csv file
states = pandas.read_csv("50_states.csv")
states_names = states["state"].tolist()
x_coordinates = states["x"].tolist()
y_coordinates = states["y"].tolist()

# Game play
# User input
states_correct = 0
guesses = 50
guessed_states = []
states_to_learn = []


# Function Definition
def add_states(x, y, name):
    text.penup()
    text.hideturtle()
    text.goto(x, y)
    text.write(name)


answer = str(screen.textinput(title="Guess the State", prompt="What is the state's name?")).title()

while guesses > 0:
    guesses -= 1

    if answer == "Exit":
        for state in states_names:
            if state not in guessed_states:
                states_to_learn.append(state)
        learn = pandas.DataFrame(states_to_learn)
        learn.to_csv("States To Learn.csv")
        break

    for state in states_names:
        if answer == state:
            states_correct += 1
            guessed_states.append(state)
            index = states_names.index(state)
            x_cor = x_coordinates[index]
            y_cor = y_coordinates[index]
            add_states(x_cor, y_cor, state)

    answer = str(screen.textinput(title=f"{states_correct}/{TOTAL_STATES} Correct",
                                  prompt="What is the state's name?")).title()

