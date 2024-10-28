import sys
import random
from functools import partial
from PySide6 import QtWidgets 
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow
import randnum

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.buttons = ([self.ui.btn1,self.ui.btn2,self.ui.btn3,self.ui.btn4],
                        [self.ui.btn5,self.ui.btn6,self.ui.btn7,self.ui.btn8],
                        [self.ui.btn9,self.ui.btn10,self.ui.btn11,self.ui.btn12],
                        [self.ui.btn13,self.ui.btn14,self.ui.btn15,self.ui.btn16])
        my_list = randnum (4,4,1,16)
        for i in range(4):
            for j in range (4):
                n = my_list[i][j]
                self.buttons[i][j].setText(str(n))
                self.buttons[i][j].clicked.connect(partial(self.play.i.j))
                if n==16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i = i
                    self.empty_j = j

    def play(self,i,j):

        if(i == self.empty_i and abs(j - self.empty_j) == 1) or\
           (j == self.empty_j and abs(i- self.empty_i) == 1):
           self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].toPlainText())
           self.buttons[i][j].setText(self.buttons[self.empty_i][self.empty_j].toPlainText())#"16"
           self.buttons[self.empty_i][self.empty_j].setVisible(True)
           self.buttons[j].setVisible(False)
           self.empty_i = i
           self.empty_j = j
        else:
          pass

        if self.check_win == True:
              ms_box = QMessageBox()
              ms_box.setText("won!!!")
              ms_box.exec()

    def check_win(self):
        index = 1
        for i in range (4):
            for j in range(4):
                if int(self.buttons[i][j].toPlainText()!= index):
                    return False
        return True
    

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()
app.exec()