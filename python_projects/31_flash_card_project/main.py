from tkinter import *
import pandas
import random

current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    #orient = Provides the keyname(key) : value name(key value) format


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card =  random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_text, text= current_card["French"], fill= "black")
    canvas.itemconfig(canvas_background, image=canvas_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_text, text= current_card["English"], fill= "white")
    canvas.itemconfig(canvas_background, image= canvas_back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    #index= False made not give the index numbers at the starting

    next_card()


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash cards")
window.config(pady=50, padx=50, bg =  BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
canvas_front_image = PhotoImage(file="images/card_front.png")
canvas_back_image = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image= canvas_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image= cross_image,  bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()