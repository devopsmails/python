#This is all about Tkinter Layout Manager:
#1.pack() : makes any component visible on the screen
#2.Place() : helps to place any widgets on specific X, y value
#3.Grid() : *Most useful* & helps assign the widgets specially as rows & columns.
            #either Grid is in use of programme should not use pack(gives an errors)
#4. Pad(): Padding helps to give space around the window screen or specific widget(padx, pady)
from tkinter import *


from tkinter import *

def button_clicked():
    print("i've got clicked")
    input_value = input.get()
    my_label.config(text = input_value )

windows = Tk()
#4
windows.config(padx= 50, pady= 50)
#Label
my_label = Label(text = "I'm a Label for this page", font= ("Arial", 14, "bold"))
my_label.grid(column=0, row=0)
#1.my_label.pack(side= "Left")
#2.my_label.place(x = 100, y = 100)


my_label.config(text = "new text" )

##Button  & command :
button = Button(text = "Click me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=50, pady=50)

#new button:

new_button = Button(text = "New button", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry:
input = Entry(width = 20 )
input_value = input.get()
input.grid(column=3, row=2)

windows.mainloop()
