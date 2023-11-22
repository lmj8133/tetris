from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QFormLayout
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from threading import Timer

class View(QWidget):
    def __init__(self, view_model):
        super().__init__()
        self.view_model = view_model
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SRS Practice")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel()
        layout.addWidget(self.label)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.game_start)
        layout.addWidget(start_button)

        config_button = QPushButton("Configuration")
        config_button.clicked.connect(self.show_configuration)
        layout.addWidget(config_button)

        self.setLayout(layout)

        #set game screen at middle
        self.label.setAlignment(Qt.AlignCenter)

        self.view_model.questionChanged.connect(self.update_question)

    def keyPressEvent(self, event):
        key = event.text()
        self.view_model.key_pressed(key)

    def game_start(self):
        self.view_model.keyChanged.connect(self.show_result)
        self.view_model.shuffle_question()

    def show_configuration(self):
        config_dialog = ConfigurationDialog(self.view_model, self)
        config_dialog.exec_()


    @pyqtSlot(str)
    def update_question(self, path):
        self.label.setText(f"Question {path}.")
        self.label.setPixmap(QPixmap(path))

    def show_result(self, result):
        self.label.setText(f"{result}")

        t = Timer(0.5, self.view_model.shuffle_question)
        t.start()

class ConfigurationDialog(QDialog):
    def __init__(self, view_model, parent=None):
        super(ConfigurationDialog, self).__init__(parent)
        self.view_model = view_model
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Configuration")
        self.setGeometry(100, 100, 300, 200)

        lineEdit_ccw = QLineEdit()
        lineEdit_cw = QLineEdit()

        layout = QVBoxLayout()

        formLayout = QFormLayout()
        formLayout.addRow("Counter Clockwise", lineEdit_ccw)
        formLayout.addRow("Clockwise", lineEdit_cw)
        layout.addLayout(formLayout)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_configuration)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_configuration(self):
        # Save configuration logic here
        self.accept()
