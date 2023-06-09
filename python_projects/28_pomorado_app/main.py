from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    windows.after_cancel(timer)
    #Helps stops the running timer

    timer_label.config(text="Timer")
    canvas.itemconfig(canvas_timer, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED, bg= YELLOW,  font=(FONT_NAME, 30, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    else:
        count_down(work_seconds)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds <10:
        seconds  = f"0{seconds}"

    canvas.itemconfig(canvas_timer, text= f"{minutes} : {seconds}")
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Pomorodo Technique")
windows.config(padx= 100, pady = 50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, bg= YELLOW,  font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0,)

canvas = Canvas(width= 202, height=224, bg=YELLOW, highlightthickness=0)
# highlightthickness = we can increase or decrease any hightlightthickness or we make to 0 = not visible

tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomoto_img)
canvas_timer = canvas.create_text(100, 135, text = "00:00", fill= "white", font=(FONT_NAME, 25, "bold" ) )
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

restart_button = Button(text="Reset", command=reset)
restart_button.grid(column=2, row=2)

check_mark = Label(fg= GREEN,bg= YELLOW,  font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=3)

windows.mainloop()