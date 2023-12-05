import sys
import ViewModel
from View import *
from Model import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = main_page.View()
    model = main_model.Model()
    vm = ViewModel.core.VM(view, model)
    view.show()

    sys.exit(app.exec_())

