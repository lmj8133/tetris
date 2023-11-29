from Model.model import Model
from PyQt5.QtCore import pyqtSignal, QObject

class ViewModel(QObject):
    keyChanged = pyqtSignal(str)

    def __init__(self, view, model):
        super().__init__()
        self.model = model
        self.view = view
        # Connect to the View signal
        self.view.shuffleQuestionSignal.connect(self.shuffle_question) 
        self.view.gameStartSignal.connect(self.game_start)
        self.view.getConfigSignal.connect(self.getConfig)
        self.view.keyPressEventSignal.connect(self.key_pressed)
        # Connect to the Model signal
        self.model.questionChanged.connect(self.forward_question_changed)

    def forward_question_changed(self, path):
        self.view.update_question(path)

    def key_pressed(self, key):
        self.keyChanged.emit(self.model.return_answer(key))

    def shuffle_question(self):
        self.model.shuffle_question()

    def getConfig(self):
        self.model.getConfig()

    def game_start(self):
        self.keyChanged.connect(self.view.show_result)
        self.shuffle_question()

