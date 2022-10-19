import requests
import html
import customtkinter
from tkinter import PhotoImage


def get_question(amount):
    if amount > 50:
        amount = 50
    elif amount < 1:
        amount = 1

    api_endpoint = "https://opentdb.com/api.php"
    parameter = {
        "amount": amount,
        "type": "boolean",
    }

    question = requests.get(api_endpoint, params=parameter)
    question.raise_for_status()
    question = question.json()["results"]

    questions = [
        {"question": html.unescape(i["question"]), "ans": i["correct_answer"]}
        for i in question
    ]

    return questions


def reset(q_number):
    question_box.config(bg="white")
    question_box.itemconfig(question_text, text=questions[q_number]["question"])


def question_motion(answer):
    global question_number, score

    if questions[question_number]["ans"] == answer:
        question_box.config(bg="green")
        score += 1
        score_label.configure(text=f"Score: {score}")
    else:
        question_box.config(bg="red")

    question_number += 1
    window.after(1000, reset, question_number)


questions = get_question(50)
question_number = 0

window = customtkinter.CTk()

window.title("Question Game")
window.set_appearance_mode("Dark")
window.geometry("440x800")
window.config(padx=20, pady=50)

# Score
score = 0
bg_color = "#212325"

# Images
right = PhotoImage(
    file="New_Shit__/Angela_Yu__/Day_34 #Question_game_with_trivia_api/question_game/right.png"
)
wrong = PhotoImage(
    file="New_Shit__/Angela_Yu__/Day_34 #Question_game_with_trivia_api/question_game/wrong.png"
)


# Label
score_label = customtkinter.CTkLabel(
    text=f"Score: {score}", fg="white", text_font=("Courier", 20)
)


# Question Canvas
question_box = customtkinter.CTkCanvas(
    width=400, height=500, highlightthickness=0, border=False
)
question_text = question_box.create_text(
    200,
    200,
    text=questions[question_number]["question"],
    justify="center",
    font=("Courier", 20, "bold"),
    width=350,
)

# Buttons
right_button = customtkinter.CTkButton(
    text="",
    fg_color=bg_color,
    image=right,
    highlightthickness=0,
    border=False,
    width=0,
    command=lambda: question_motion("True"),
)
wrong_button = customtkinter.CTkButton(
    text="",
    fg_color=bg_color,
    image=wrong,
    highlightthickness=0,
    border=False,
    width=0,
    command=lambda: question_motion("False"),
)

# Griding
score_label.grid(row=0, column=1)
question_box.grid(row=1, column=0, columnspan=2)
right_button.grid(row=2, column=0, pady=10)
wrong_button.grid(row=2, column=1, pady=10)


window.mainloop()
