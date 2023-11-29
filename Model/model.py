import json
from random import choice
from PyQt5.QtCore import QObject, pyqtSignal

class Model(QObject):
    questionChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.getConfig()
        self.shuffle_question()

    def check_answer(self, key):
        if key == self.question.answer:
            self.result = 'Right'
        else:
            self.result = 'Wrong'

    def shuffle_question(self):
        sequence = [self.question_J_CW, self.question_J_CCW, self.question_L_CW, self.question_L_CCW, self.question_T_CW, self.question_T_CCW]
        self.question = choice(sequence)
        self.questionChanged.emit(self.question.path)

    def getConfig(self):
        with open('./Config/config.json', 'r') as json_file:
            config = json.load(json_file)
            # CW for counterwise; CCW for counterclockwise
            self.answer_cw = config.get('cw', '')
            self.answer_ccw = config.get('ccw', '')
            self.question_J_CW = Question("./pictures/J-CW.png", self.answer_cw)
            self.question_J_CCW = Question("./pictures/J-CCW.png", self.answer_ccw)
            self.question_L_CW = Question("./pictures/L-CW.png", self.answer_cw)
            self.question_L_CCW = Question("./pictures/L-CCW.png", self.answer_ccw)
            self.question_T_CW = Question("./pictures/T-CW.png", self.answer_cw)
            self.question_T_CCW = Question("./pictures/T-CCW.png", self.answer_ccw)

class Question:
    def __init__(self, path, answer):
        self.path = path
        self.answer = answer

