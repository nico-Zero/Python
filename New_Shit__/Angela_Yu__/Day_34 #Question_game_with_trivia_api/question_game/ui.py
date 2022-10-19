import customtkinter
from tkinter import PhotoImage

BG_COLOR = "#212325"


class QuizGameUi:
    def __init__(self, brain):
        self.quiz = brain
        self.window = customtkinter.CTk()

        self.window.title("Question Game")
        self.window.set_appearance_mode("Dark")
        self.window.geometry("440x800")
        self.window.config(padx=20, pady=50)

        # Images
        right = PhotoImage(
            file="New_Shit__/Angela_Yu__/Day_34 #Question_game_with_trivia_api/question_game/right.png"
        )
        wrong = PhotoImage(
            file="New_Shit__/Angela_Yu__/Day_34 #Question_game_with_trivia_api/question_game/wrong.png"
        )

        # Label
        self.score_label = customtkinter.CTkLabel(
            text=f"Score: {self.quiz.get_score()}",
            fg="white",
            text_font=("Courier", 20),
        )

        # Question Canvas
        self.question_box = customtkinter.CTkCanvas(
            width=400, height=500, highlightthickness=0, border=False
        )
        self.question_text = self.question_box.create_text(
            200,
            200,
            text=self.quiz.question()["question"],
            justify="center",
            font=("Courier", 20, "bold"),
            width=350,
        )

        # Buttons
        self.right_button = customtkinter.CTkButton(
            text="",
            fg_color=BG_COLOR,
            image=right,
            highlightthickness=0,
            border=False,
            width=0,
            command=lambda: self.question_motion("True"),
        )
        self.wrong_button = customtkinter.CTkButton(
            text="",
            fg_color=BG_COLOR,
            image=wrong,
            highlightthickness=0,
            border=False,
            width=0,
            command=lambda: self.question_motion("False"),
        )

        # Griding
        self.score_label.grid(row=0, column=1)
        self.question_box.grid(row=1, column=0, columnspan=2)
        self.right_button.grid(row=2, column=0, pady=10)
        self.wrong_button.grid(row=2, column=1, pady=10)

        self.window.mainloop()

    def question_motion(self, answer):
        if self.quiz.check_answer(answer):
            self.question_box.config(bg="green")
            self.score_label.configure(text=f"Score: {self.quiz.get_score()}")
        else:
            self.question_box.config(bg="red")

        self.window.after(1000, self.reset, self.quiz.question()["question"])

    def reset(self, question):
        self.question_box.config(bg="white")
        self.question_box.itemconfig(self.question_text, text=question)
