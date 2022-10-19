import requests
import html
from quiz_brain import Brain
from ui import QuizGameUi

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

questions = get_question(50)

brain = Brain(questions)
ui = QuizGameUi(brain)
