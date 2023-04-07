import turtle
import pandas


screen = turtle.Screen()
screen.title("US.data Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) <49:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50",
                                    prompt="What is another state?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("need_to_learn.csv")
        break # breaks the loop

    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)
        #another way

        ##tim.write(state_data.data.item())



