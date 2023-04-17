doc: https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html

#This is mainly about
# button : Which helps to create some value
# command: Helps to route button to next info
# Entry : Helps to give space to write or enter something
# Get : get will hold / fetch the value of  Entry

#1 import tkinter single class

import tkinter

#2 or to import every class  from the tkinter(instead of specifying the class & using the module we can directly call the module)

from tkinter import *


#1 windows = tkinter.Tk()

#2
windows = Tk()

windows.title("This is My First GUI Program")
windows.minsize(width= 500, height=300)

##lebel
#1 my_label = tkinter.Label(text = "I'm a Label for this page", font= ("Arial", 14, "bold"))
#2
my_label = Label(text = "I'm a Label for this page", font= ("Arial", 14, "bold"))
my_label.pack()

my_label["text"] = "New text"

## or
my_label.config(text = "new text" )

##Button = Helps to route to another info

def button_clicked():
    print("i've got clicked")
    input_value = input.get()
    my_label.config(text = input_value )

#command = routes the button to specific info

button = Button(text = "Click me", command=button_clicked)
button.pack()

#Entry

input = Entry(width = 40 )
input_value = input.get()
input.pack()

windows.mainloop()
