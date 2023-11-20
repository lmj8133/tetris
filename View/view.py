from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot

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

        inc_button = QPushButton("Increment")
        inc_button.clicked.connect(self.view_model.increment)
        layout.addWidget(inc_button)

        dec_button = QPushButton("Decrement")
        dec_button.clicked.connect(self.view_model.decrement)
        layout.addWidget(dec_button)

        self.setLayout(layout)

        self.view_model.valueChanged.connect(self.update_label)
        self.view_model.model.key_changed.connect(self.update_key)

    def keyPressEvent(self, event):
        key = event.text()
        self.view_model.key_pressed(key)

    @pyqtSlot(int)
    def update_label(self, value):
        self.label.setText(f"Counter: {value}")

    @pyqtSlot(str)
    def update_key(self, key):
        self.label.setText(f"Key: {key}")
