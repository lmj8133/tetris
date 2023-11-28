import sys
from PyQt5.QtWidgets import QApplication
from ViewModel.viewModel import ViewModel
from View.view import View
from Model.model import Model

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    model = Model()
    view_model = ViewModel(view, model)

    view.show()
    sys.exit(app.exec_())

