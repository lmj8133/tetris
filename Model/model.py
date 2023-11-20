from PyQt5.QtCore import QObject, pyqtSignal

class Model(QObject):
    valueChanged = pyqtSignal(int)
    key_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.value = 0

    def increment(self):
        self.value += 1
        self.valueChanged.emit(self.value)

    def decrement(self):
        self.value -= 1
        self.valueChanged.emit(self.value)

    def set_key(self, key):
        self.key_changed.emit(key)
