from Model.model import Model
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject

class ViewModel(QObject):
    keyChanged = pyqtSignal(str)
    questionChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.model = Model()
        #self.shuffle_question()

    def key_pressed(self, key):
        self.model.check_answer(key)
        self.keyChanged.emit(self.model.result)

    def shuffle_question(self):
        self.loadConfig()
        self.questionChanged.emit(self.model.question.path)

    def getConfig(self):
        self.model.getConfig()

    def loadConfig(self):
        self.model.shuffle_question()
