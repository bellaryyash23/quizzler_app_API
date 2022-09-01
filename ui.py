from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Question_text", font=FONT, fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, foreground="white", pady=10, font="Courier")
        self.score_label.grid(row=0, column=1)

        correct_btn_img = PhotoImage(file="./images/true.png")
        wrong_btn_img = PhotoImage(file="./images/false.png")

        self.correct_btn = Button(image=correct_btn_img, highlightthickness=0, command=self.true_pressed)
        self.correct_btn.grid(row=2, column=0)

        self.wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_btn.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've ended the Quiz")
            self.correct_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
