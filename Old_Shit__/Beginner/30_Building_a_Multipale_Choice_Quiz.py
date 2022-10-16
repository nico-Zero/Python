from Question import Question

question_prompt = [
    "What color are apples?\n(a) Red/Green\n(b) Blue\n(c) Orange\n\n:",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n:",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n:",
    "What color are my hand?\n(a) Yellow\n(b) Red\n(c) White\n\n:"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),
    Question(question_prompt[3], "c")
]


def run(questions):
    score = 0
    for question in questions:
        answer = input(question.promt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run(questions)
