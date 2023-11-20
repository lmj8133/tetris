from PyQt5.QtCore import QObject

class Model(QObject):

    def __init__(self):
        super().__init__()
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1
