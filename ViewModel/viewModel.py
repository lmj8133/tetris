from Model.model import Model
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject

class ViewModel(QObject):
    valueChanged = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.model = Model()

    def increment(self):
        self.model.increment()
        self.valueChanged.emit(self.model.value)

    def decrement(self):
        self.model.decrement()
        self.valueChanged.emit(self.model.value)

    def key_pressed(self, key):
        self.model.set_key(key)
