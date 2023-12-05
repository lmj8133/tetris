import json
from threading import Timer
from random import choice
from PyQt5.QtCore import QObject

class Model(QObject):
    def __init__(self):
        super().__init__()
        
        '''
        define variable
        '''
        self.game_label_text = ""
        self.game_label_img = ""
        self.editor_text = 'welcome!!!'
        self.start_btn_text = 'Start' 
        self.start_btn_enable = True
        self.getConfig()

        '''
        define key of variable
        '''
        def mapEditorTextKey(val=None):
            if val != None: self.editor_text = val
            else:           return self.editor_text 

        def mapStartBtnTextKey(val=None):
            if val != None: self.start_btn_text = val
            else:           return self.start_btn_text 

        def mapStartBtnEnableKey(val=None):
            if val != None: self.start_btn_enable = val
            else:           return self.start_btn_enable 

        def mapLabelTextKey(val=None):
            if val != None: self.game_label_text = val
            else:           return self.game_label_text 

        def mapLabelImgKey(val=None):
            if val != None: self.game_label_img = val
            else:           return self.game_label_img 

        self.data_key = {
            'lebel_text': mapLabelTextKey,
            'label_img': mapLabelImgKey,
            'editor_text': mapEditorTextKey,
            'start_btn_text': mapStartBtnTextKey,
            'start_btn_enable': mapStartBtnEnableKey,
        }
        self.w2f_key = {
            'start_btn_click': self.game_start,
            'key_press': self.key_pressed,
            'cfg_save_btn_click': self.getConfig
        }

    def key_pressed(self, key):
        print(self.editor_text)
        if key == self.question.answer: self.game_label_text = 'Right'
        else:                           self.game_label_text = 'Wrong'
        Timer(0.5, self.shuffle_question).start()

    def shuffle_question(self):
        sequence = [self.question_J_CW, self.question_J_CCW, self.question_L_CW, self.question_L_CCW, self.question_T_CW, self.question_T_CCW]
        self.question = choice(sequence)
        self.game_label_text = 'please answer'
        self.game_label_img = self.question.path

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

    def game_start(self):
        self.start_btn_enable = False
        self.editor_text = 'game beginning...'
        self.shuffle_question()
    
class Question:
    def __init__(self, path, answer):
        self.path = path
        self.answer = answer

