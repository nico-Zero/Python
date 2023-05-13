class Brain:
    def __init__(self, list):
        self.questions = list
        self.question_number = 0
        self.score = 0
        self.error = 0

    def question(self) -> str:
        x = self.questions[self.question_number]["question"]
        self.question_number += 1
        return x

    def get_score(self):
        return self.score

    def check_answer(self, answer):
        if answer == self.questions[self.question_number]["ans"]:
            self.score += 1
            return True
        else:
            return False

    def still_question(self):
        if self.question_number >= len(self.questions):
            return False
        else:
            return True