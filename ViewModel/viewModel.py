from Model.model import Model
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject

class ViewModel(QObject):
    valueChanged = pyqtSignal(int)
    key_changed = pyqtSignal(str)
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
        self.key_changed.emit(key)
