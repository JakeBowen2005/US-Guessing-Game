import turtle as t
import pandas
import csv

screen = t.Screen()
screen.title("US States")
img = "blank_states_img.gif"
screen.addshape(img)
t.shape(img)

data = pandas.read_csv("50_states.csv")

correct = 0
game = True

#game dictionary
game_dict = data.to_dict()

#get list of all states
states = data["state"].to_list()
# x = data[data.state == "Texas"]["x"].iloc[0]
# print(x)

# def get_mouse(x, y):
#     print(x, y)
# t.onscreenclick(get_mouse)
while game:
    answer_state = screen.textinput(title=f"{correct}/50  Guess the State", prompt="What's the State's name").title()
    if answer_state in states:
        state_name = t.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.color("Black")
        #have to get the x and y cordinate from corresponding state
        # x_cor = data[data.state == answer_state]["x"].iloc[0]
        # y_cor = data[data.state == answer_state]["y"].iloc[0]
        state_data = data[data.state == answer_state]
        state_name.goto(x=int(state_data.x.item()), y=int(state_data.y.item())) # item just gets the item without the row it is in
        state_name.write(arg=answer_state, font=("Arial", 8, "normal"), align="center", move=False)
        correct += 1
    if correct == 50:
        game = False


t.mainloop()
