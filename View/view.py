import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QFormLayout, QMessageBox
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

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.game_start)
        layout.addWidget(self.start_button)

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
        self.start_button.setEnabled(False)
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
    def __init__(self, view_model, view):
        super(ConfigurationDialog, self).__init__()
        self.view_model = view_model
        self.view = view
        self.init_ui()
        self.loadDefaultConfig()

    def init_ui(self):
        self.setWindowTitle("Configuration")
        self.setGeometry(100, 100, 300, 200)

        self.lineEdit_ccw = QLineEdit()
        self.lineEdit_cw = QLineEdit()

        self.lineEdit_ccw.setMaxLength(1)
        self.lineEdit_cw.setMaxLength(1)

        layout = QVBoxLayout()

        formLayout = QFormLayout()
        formLayout.addRow("Counter Clockwise", self.lineEdit_ccw)
        formLayout.addRow("Clockwise", self.lineEdit_cw)
        layout.addLayout(formLayout)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_configuration)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_configuration(self):
        # Save configuration logic here
        self.saveToJson()
        self.accept()
        self.view_model.getConfig()
        if not self.view.start_button.isEnabled():
            self.view_model.shuffle_question()

    def saveToJson(self):
        if self.lineEdit_ccw.text() and self.lineEdit_cw.text():
            try:
                with open('Config/config.json', 'w') as json_file:
                    json.dump({'ccw' : self.lineEdit_ccw.text(), 'cw' : self.lineEdit_cw.text()}, json_file)
                    QMessageBox.information(self, 'Saved', 'Data saved to ./Config/config.json')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error saving configuration: {str(e)}')
        else:
            QMessageBox.warnint(self, 'Empty Input', 'Please enter some text in both fields before saving.')
            
    def loadDefaultConfig(self):
        with open('Config/config.json', 'r') as json_file:
            config= json.load(json_file)
            self.lineEdit_ccw.setText(config.get('ccw', ''))
            self.lineEdit_cw.setText(config.get('cw', ''))
