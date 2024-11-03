import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_main import Ui_MainWindow




class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.remover)
            
           
               
            

    
    def remover (self):
        self.text2 = self.ui.textEdit.toPlainText()
        result = self.text2.replace('\n', ' ')
        self.ui.textEdit_2.setText(result)



    



app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()
app.exec()