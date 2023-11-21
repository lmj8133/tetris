from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from threading import Timer

class View(QWidget):
    def __init__(self, view_model):
        super().__init__()
        self.view_model = view_model
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Application")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel()
        layout.addWidget(self.label)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.view_model.shuffle_question)
        layout.addWidget(start_button)

        self.setLayout(layout)

        self.label.setPixmap(QPixmap(self.view_model.model.question.path))

        self.view_model.valueChanged.connect(self.update_label)
        self.view_model.keyChanged.connect(self.update_key)
        self.view_model.questionChanged.connect(self.update_question)

    def keyPressEvent(self, event):
        key = event.text()
        self.view_model.key_pressed(key)

    @pyqtSlot(int)
    def update_label(self, value):
        self.label.setText(f"Counter: {value}")

    @pyqtSlot(str)
    def update_question(self, path):
        self.label.setText(f"Question {path}.")
        self.label.setPixmap(QPixmap(path))

    def update_key(self, result):
        self.label.setText(f"{result}")
        t = Timer(0.5, self.view_model.shuffle_question)
        t.start()
