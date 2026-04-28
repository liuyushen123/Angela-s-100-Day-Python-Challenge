import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.canvas = tk.Canvas(background="white", height=250, width=300)
        self.false_image = tk.PhotoImage(file="images/false.png")
        self.true_image = tk.PhotoImage(file="images/true.png")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Text",
            fill="black",
            justify="center",
            width=285,
            font=("Arial", 20, "italic"),
        )
        self.score_label = tk.Label(
            text=f"Score: {self.score}",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.correct_button = tk.Button(
            image=self.true_image,
            command=self.true_pressed,
        )
        self.wrong_button = tk.Button(
            image=self.false_image,
            command=self.false_pressed,
        )

        self.score_label.grid(
            column=1,
            row=0,
        )

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.correct_button.grid(
            column=0,
            row=2,
        )
        self.wrong_button.grid(
            column=1,
            row=2,
        )
        self.show_question()
        self.window.mainloop()

    def show_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.score_label.grid_forget()
            self.canvas.itemconfig(
                self.question_text,
                text=f"That's everything!\n Your Final Score: {self.quiz.score} out of {len(self.quiz.question_list)}",
            )
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        print(is_right)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.show_question)
