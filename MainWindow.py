from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Einführung ins QMainWindow")

        #self.setMinimumWidth(480)
        #self.setMinimumHeight(600)

        #self.setMaximumWidth(800)
        #self.setMaximumHeight(1024)

        central_widget = CentralWidget(self)
        self.setCentralWidget(central_widget)