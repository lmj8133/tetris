from PyQt5.QtCore import QObject


class Model(QObject):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.result = 'Right'
        self.question = Question("./pictures/J-D.png", "d")

    def key_m(self, key):
        if key == self.question.answer:
            self.result = 'Right'
        else:
            self.result = 'Wrong'

    def shuffle_question(self):
        self.question = Question("./pictures/J-D.png", "d")

class Question(Model):
    def __init__(self, path, answer):
        self.path = path
        self.answer = answer
