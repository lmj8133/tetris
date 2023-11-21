from PyQt5.QtCore import QObject
from random import choice


class Model(QObject):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.result = 'Right'
        self.question_JD = Question("./pictures/J-D.png", "d")
        self.question_JA = Question("./pictures/J-A.png", "a")
        self.question_LD = Question("./pictures/L-D.png", "d")
        self.question_LA = Question("./pictures/L-A.png", "a")
        self.question_TD = Question("./pictures/T-D.png", "d")
        self.question_TA = Question("./pictures/T-A.png", "a")
        self.shuffle_question()

    def key_m(self, key):
        if key == self.question.answer:
            self.result = 'Right'
        else:
            self.result = 'Wrong'

    def shuffle_question(self):
        sequence = [self.question_JD, self.question_JA, self.question_LD, self.question_LA, self.question_TD, self.question_TA]
        self.question = choice(sequence)

class Question(Model):
    def __init__(self, path, answer):
        self.path = path
        self.answer = answer
