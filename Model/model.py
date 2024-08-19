import json
from random import choice
from PyQt5.QtCore import QObject, pyqtSignal

class Model(QObject):
    questionChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.getConfig()
        self.shuffle_question()

    # Check & return answer
    def return_answer(self, key):
        if key == self.question.answer:
            self.result = 'Right'
        else:
            self.result = 'Wrong'
        return self.result

    def shuffle_question(self):
        sequence = [self.question_J_CW, self.question_J_CCW, self.question_L_CW, self.question_L_CCW, self.question_T_CW, self.question_T_CCW, self.question_J_180, self.question_L_180, self.question_T_180]
        self.question = choice(sequence)
        self.questionChanged.emit(self.question.path)

    def getConfig(self):
        with open('./Config/config.json', 'r') as json_file:
            config = json.load(json_file)
            # CW for counterwise; CCW for counterclockwise; 180 for 180 degree
            self.answer_cw = config.get('cw', '')
            self.answer_ccw = config.get('ccw', '')
            self.answer_180 = config.get('180', '')
            self.question_J_CW = Question("./pictures/J-CW.png", self.answer_cw)
            self.question_J_CCW = Question("./pictures/J-CCW.png", self.answer_ccw)
            self.question_J_180 = Question("./pictures/J-180.png", self.answer_180)
            self.question_L_CW = Question("./pictures/L-CW.png", self.answer_cw)
            self.question_L_CCW = Question("./pictures/L-CCW.png", self.answer_ccw)
            self.question_L_180 = Question("./pictures/L-180.png", self.answer_180)
            self.question_T_CW = Question("./pictures/T-CW.png", self.answer_cw)
            self.question_T_CCW = Question("./pictures/T-CCW.png", self.answer_ccw)
            self.question_T_180 = Question("./pictures/T-180.png", self.answer_180)

class Question:
    def __init__(self, path, answer):
        self.path = path
        self.answer = answer

