from PyQt5.QtCore import QObject, pyqtSignal, QThread
import time
class VM(QObject):
    flushSignal = pyqtSignal()
    def __init__(self, view, model):
        super().__init__()
        self.model = model
        self.view = view
        self.flush_history = {}

        # binding view and model.data
        for key in view.data_key:
            view.data_key[key](model.data_key[key]())
            self.flush_history[key] = model.data_key[key]()

        # binding vew to model.method
        for key in view.w2f_key:
            view.w2f_key[key].connect(model.w2f_key[key])
        
        self.flushSignal.connect(self.flush)
        self.thread_a = QThread()
        self.thread_a.run = self.flush_task
        self.thread_a.start()

    def flush(self):
        for key in self.model.data_key:
            if(self.flush_history[key] != self.model.data_key[key]()):
                self.view.data_key[key](self.model.data_key[key]())
                self.flush_history[key] = self.model.data_key[key]()
            elif (self.flush_history[key] != self.view.data_key[key]()):
                self.model.data_key[key](self.view.data_key[key]())
                self.flush_history[key] = self.model.data_key[key]()

    def flush_task(self):        
        while True:
            time.sleep(0.1)
            self.flushSignal.emit()
