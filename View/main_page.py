import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QFormLayout, QMessageBox, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

class View(QWidget):
    keyPressEventSignal = pyqtSignal(str)
    startBtnSignal = pyqtSignal()
    cfgBtnSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        '''
        define UI
        '''
        self.setWindowTitle("Tetris")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel('default')
        layout.addWidget(self.label)

        self.label_img = QLabel('default')
        layout.addWidget(self.label_img)

        self.text_edit = QTextEdit('default')
        layout.addWidget(self.text_edit)
    
        self.start_button = QPushButton('default')
        self.start_button.clicked.connect(self.start_btn_click)
        layout.addWidget(self.start_button)

        self.config_button = QPushButton('Configuration')
        self.config_button.clicked.connect(self.cfg_btn_click)
        layout.addWidget(self.config_button)

        self.setLayout(layout)

        #set game screen at middle
        self.label.setAlignment(Qt.AlignCenter)

        '''
        define key of widget
        '''
        def mapTextEditorKey(val=None):
            if val != None: self.text_edit.setPlainText(val)
            else:           return self.text_edit.toPlainText()

        def mapStartBtnTextKey(val=None):
            if val != None: self.start_button.setText(val)
            else:           return self.start_button.text()

        def mapStartBtnEnableKey(val=None):
            if val != None: self.start_button.setEnabled(val)
            else:           return self.start_button.isEnabled()

        def mapLabelTextKey(val=None):
            if val != None: self.label.setText(val)
            else:           return self.label.text()

        def mapLabelImgKey(val=None):
            if val != None: self.label_img.setPixmap(QPixmap(val))

        self.data_key = {
            'lebel_text': mapLabelTextKey,
            'label_img': mapLabelImgKey,
            'editor_text': mapTextEditorKey,
            'start_btn_text': mapStartBtnTextKey,
            'start_btn_enable': mapStartBtnEnableKey,
        }
        self.w2f_key = {
            'start_btn_click': self.startBtnSignal,
            'key_press': self.keyPressEventSignal,
            'cfg_save_btn_click': self.cfgBtnSignal
        }

    def start_btn_click(self):
        self.startBtnSignal.emit()

    def keyPressEvent(self, event):
        key = event.text()
        self.keyPressEventSignal.emit(key)

    def cfg_btn_click(self):
        config_dialog = ConfigurationDialog(self)
        config_dialog.exec_()

class ConfigurationDialog(QDialog):
    def __init__(self, view):
        super(ConfigurationDialog, self).__init__()
        self.view = view
        self.__init_ui()
        self.loadDefaultConfig()

    def __init_ui(self):
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
        self.saveToJson()
        self.accept()
        self.view.cfgBtnSignal.emit()

    def saveToJson(self):
        if self.lineEdit_ccw.text() and self.lineEdit_cw.text():
            try:
                with open('Config/config.json', 'w') as json_file:
                    json.dump({'ccw' : self.lineEdit_ccw.text(), 'cw' : self.lineEdit_cw.text()}, json_file)
                    QMessageBox.information(self, 'Saved', 'Data saved to ./Config/config.json')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error saving configuration: {str(e)}')
        else:
            QMessageBox.warning(self, 'Empty Input', 'Please enter some text in both fields before saving.')
            
    def loadDefaultConfig(self):
        with open('Config/config.json', 'r') as json_file:
            config= json.load(json_file)
            self.lineEdit_ccw.setText(config.get('ccw', ''))
            self.lineEdit_cw.setText(config.get('cw', ''))
