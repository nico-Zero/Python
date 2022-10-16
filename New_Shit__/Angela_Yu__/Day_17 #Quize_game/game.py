from random import choice


class Game:
    def __init__(self, game_questions):
        self.questions = game_questions
        self.score = 0
        self.t_f = {"t": "true", "f": "false", "T": "true", "F": "false"}

    def question(self):
        try:
            q = choice(self.questions)
            self.questions.remove(q)
            return q
        except Exception:
            print("Game Over!")
            return "Game Over!"

    def answer(self, x, y):
        if y in self.t_f:
            y = self.t_f[y]

        if y.lower() == x.lower():
            self.score += 1
        else:
            pass
