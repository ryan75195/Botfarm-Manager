from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import Main

class ExampleApp(QtWidgets.QMainWindow, Main.uiCode):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setUpButtons()

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
