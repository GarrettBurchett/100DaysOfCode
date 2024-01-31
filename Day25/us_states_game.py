import turtle
import pandas as pd

def correct_state(states_df, state):
    states_turtle = turtle.Turtle()
    states_turtle.hideturtle()
    states_turtle.penup()
    states_turtle.goto(int(states_df[states_df.state == state].x.iloc[0]), int(states_df[states_df.state == state].y.iloc[0]))
    states_turtle.write(state)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("Day25/50_states.csv")

score = 0
guessed_states = []
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another US State name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states.state.to_list() if state not in guessed_states]
        missing_answers = pd.DataFrame(missing_states)
        missing_answers.to_csv("Day25/states_to_learn.csv")
        break
    while answer_state not in states.state.to_list():
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another US State name?").title()

    correct_state(states, answer_state)
    guessed_states.append(answer_state)
    score += 1

screen.exitonclick()