import json
from random import choice

class Model:
    def __init__(self):
        super().__init__()
        self.answer_cw = "d"
        self.answer_ccw = "a"
        self.getConfig()
        self.question_JD = Question("./pictures/J-D.png", self.answer_cw)
        self.question_JA = Question("./pictures/J-A.png", self.answer_ccw)
        self.question_LD = Question("./pictures/L-D.png", self.answer_cw)
        self.question_LA = Question("./pictures/L-A.png", self.answer_ccw)
        self.question_TD = Question("./pictures/T-D.png", self.answer_cw)
        self.question_TA = Question("./pictures/T-A.png", self.answer_ccw)
        self.shuffle_question()

    def check_answer(self, key):
        if key == self.question.answer:
            self.result = 'Right'
        else:
            self.result = 'Wrong'

    def shuffle_question(self):
        sequence = [self.question_JD, self.question_JA, self.question_LD, self.question_LA, self.question_TD, self.question_TA]
        self.question = choice(sequence)

    def getConfig(self):
        with open('./Config/config.json', 'r') as json_file:
            config = json.load(json_file)
            self.answer_cw = config.get('cw', '')
            self.answer_ccw = config.get('ccw', '')
            self.question_JD = Question("./pictures/J-D.png", self.answer_cw)
            self.question_JA = Question("./pictures/J-A.png", self.answer_ccw)
            self.question_LD = Question("./pictures/L-D.png", self.answer_cw)
            self.question_LA = Question("./pictures/L-A.png", self.answer_ccw)
            self.question_TD = Question("./pictures/T-D.png", self.answer_cw)
            self.question_TA = Question("./pictures/T-A.png", self.answer_ccw)

class Question(Model):
    def __init__(self, path, answer):
        self.path = path
        self.answer = answer
