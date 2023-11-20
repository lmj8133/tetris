from Model.model import Model
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject

class ViewModel(QObject):
    valueChanged = pyqtSignal(int)
    keyChanged = pyqtSignal(str)
    questionChanged = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.model = Model()

    def key_pressed(self, key):
        self.model.key_m(key)
        self.keyChanged.emit(self.model.result)

    def shuffle_question(self):
        self.model.shuffle_question()
        self.questionChanged.emit(self.model.question.path)
