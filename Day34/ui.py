import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        check_image = tk.PhotoImage(file="Day34/images/true.png")
        self.check_button = tk.Button(image=check_image, highlightthickness=0, command=self.answer_true)
        self.check_button.grid(column=0, row=2)

        x_image = tk.PhotoImage(file="Day34/images/false.png")
        self.x_button = tk.Button(image=x_image, highlightthickness=0, command=self.answer_false)
        self.x_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def answer_true(self) -> None:
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self) -> None:
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool) -> None:
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)