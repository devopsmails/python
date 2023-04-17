from tkinter import *

def calculated():
    mile = float(input1.get())
    km = float(mile * 1.60934)
    label_result.config(text = f"{km}")


windows = Tk()
windows.title("Mile to Kilometer Converter")
windows.config(padx= 20, pady=20)

#Entry
input1 = Entry(width=10)
input1.grid(row=1, column=2)

input2 = Entry(width=10)
input2.grid(row=2, column=2)

#Label
label = Label(text= "Miles")
label.grid(row=1, column=3)

label = Label(text= "is_equal_to ")
label.grid(row=2, column=0)

label_result = Label(text= "0")
label_result.grid(row=2, column=2)

label = Label(text= "Km ")
label.grid(row=2, column=3)

button = Button(text= "Calculate", command=calculated)
button.grid(row=3, column=2)


windows.mainloop()
