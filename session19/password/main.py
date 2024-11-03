import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow
import generator

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate)
        
    def generate(self):
        if self.ui.radioButton.isChecked():
            result = generator.generate_weak_password()
        elif self.ui.radioButton_2.isChecked():
            result = generator.generate_standard_password()
        elif self.ui.radioButton_3.isChecked():
            result = generator.generate_strong_password()
        else:
            result = "Please select a password strength option."
        
        self.ui.textEdit.setText(result)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()