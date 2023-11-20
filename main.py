import sys
from PyQt5.QtWidgets import QApplication
#from ..view_model import view_model
from ViewModel.viewModel import ViewModel
from View.view import View

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view_model = ViewModel()
    view = View(view_model)
    view.show()
    sys.exit(app.exec_())
