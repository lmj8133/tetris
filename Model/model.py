from PyQt5.QtCore import QObject, pyqtSignal

class Model(QObject):
    key_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def set_key(self, key):
        self.key_changed.emit(key)
