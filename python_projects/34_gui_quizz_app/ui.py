from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE = 0
FONT = ("Arial", 14, "bold")
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        SCORE = 0
        FONT = ("Arial", 14, "bold")
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.label = Label(text=f"SCORE : {SCORE}", font= FONT, bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)


        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some question",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=self.check_image, bg=THEME_COLOR, command=self.true_pressed)
        self.check_button.grid(row=2, column=0)

        self.cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.cross_image, bg=THEME_COLOR, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score : {self.quiz.score}")
            q_text = self. quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the maximum limit")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question)