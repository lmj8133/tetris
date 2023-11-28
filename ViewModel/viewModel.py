from Model.model import Model
from PyQt5.QtCore import pyqtSignal, QObject

class ViewModel(QObject):
    keyChanged = pyqtSignal(str)
    questionChanged = pyqtSignal(str)  # Add this line

    def __init__(self, view, model):
        super().__init__()
        self.model = model
        self.view = view
        self.model.questionChanged.connect(self.forward_question_changed)  # Connect to the Model signal
        self.questionChanged.connect(self.view.update_question)
        self.view.shuffleQuestionSignal.connect(self.shuffle_question) 
        self.view.gameStartSignal.connect(self.game_start)
        self.view.getConfigSignal.connect(self.getConfig)
        self.view.keyPressEventSignal.connect(self.key_pressed)

    def forward_question_changed(self, path):
        self.questionChanged.emit(path)

    def key_pressed(self, key):
        self.model.check_answer(key)
        self.keyChanged.emit(self.model.result)

    def shuffle_question(self):
        self.model.shuffle_question()

    def getConfig(self):
        self.model.getConfig()

    def game_start(self):
        self.keyChanged.connect(self.view.show_result)
        self.shuffle_question()

