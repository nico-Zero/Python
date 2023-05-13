from data import question_50_data
from game import Game
from os import system


system("cls")
data = question_50_data
quiz = Game(data)
ans = None
word = ["True", "False", "true", "false", "t", "f", "T", "F"]
ask_question = len(data)

for _ in range(ask_question):
    que = quiz.question()
    while ans not in word:
        print(f"score: {quiz.score}/{ask_question}")
        ans = input(que["question"] + " ? ")
        system("cls")
    quiz.answer(que["correct_answer"], ans)
    ans = None

print(f"Your finale score is {quiz.score}.")
