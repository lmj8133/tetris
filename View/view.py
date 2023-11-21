from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from threading import Timer

class View(QWidget):
    def __init__(self, view_model):
        super().__init__()
        self.view_model = view_model
        self.init_ui()
        self.start = False

    def init_ui(self):
        self.setWindowTitle("SRS Practice")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel()
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.label.setText("Press any key to start")
        self.label.setAlignment(Qt.AlignCenter)

        self.view_model.keyChanged.connect(self.show_result)
        self.view_model.questionChanged.connect(self.update_question)

    def keyPressEvent(self, event):
        key = event.text()
        self.view_model.key_pressed(key)

    @pyqtSlot(str)
    def update_question(self, path):
        self.label.setText(f"Question {path}.")
        self.label.setPixmap(QPixmap(path))

    def show_result(self, result):
        if self.start == False:
            self.start = True
        else:
            self.label.setText(f"{result}")

        t = Timer(0.5, self.view_model.shuffle_question)
        t.start()
