from Model.model import Model
from PyQt5.QtCore import pyqtSlot

class ViewModel:
    def __init__(self):
        self.model = Model()

    def increment(self):
        self.model.increment()

    def decrement(self):
        self.model.decrement()

    def key_pressed(self, key):
        self.model.set_key(key)
