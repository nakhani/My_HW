import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_mainwindow import Ui_MainWindow
from sudoku import Sudoku


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                self.ui.gl_game.addWidget(new_cell,i,j)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
