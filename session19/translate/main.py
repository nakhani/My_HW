import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import translate


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.translator)
        
    def translator(self):
        x= self.ui.textEdit.toPlainText()
        if self.ui.radioButton.isChecked():
            result = translate.translate_english_to_persian(x)
        elif self.ui.radioButton_2.isChecked():
            result = translate.translate_persian_to_english(x)
        else:
            result = "Please select a password strength option."
        
        self.ui.textEdit_2.setText(result)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()