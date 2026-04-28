import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
PATH = "/Users/liuyuchen/Downloads/General Coding/Udemy Course/AngelaYu_100DaysPython/Day 25/U.S. States Game/50_states.csv"
IMAGE_PATH = "/Users/liuyuchen/Downloads/General Coding/Udemy Course/AngelaYu_100DaysPython/Day 25/U.S. States Game/blank_states_img.gif"
STATE_DATA = pd.read_csv(PATH)

screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)
state_turtle = turtle.Turtle()
score = 0
all_states = STATE_DATA["state"].to_list()
guessed_states = []


answer_state = screen.textinput(
    title="Guess a State", prompt="Type any state name you can think of"
)

while (len(guessed_states) < 50) and answer_state:
    answer_state = answer_state.title()

    if answer_state in guessed_states:
        answer_state = screen.textinput(
            title="You've Guessed that state!",
            prompt="What's another state name you can think of?",
        )

    elif answer_state in all_states:
        stateData = STATE_DATA[STATE_DATA.state == answer_state]
        score += 1
        state_turtle.goto(stateData.x.item(), stateData.y.item())
        state_turtle.write(answer_state)
        guessed_states.append(answer_state)
        answer_state = screen.textinput(
            title=f"State Correct {score}/50",
            prompt="What's another state name you can think of?",
        )

    else:
        answer_state = screen.textinput(
            title="Incorrect! ",
            prompt="What's another state name you can think of?",
        )

missing_states = [state for state in all_states if state not in guessed_states]
print(missing_states)
pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
screen.exitonclick()
