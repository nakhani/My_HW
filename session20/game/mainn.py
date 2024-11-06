import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
import random


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.about)
        self.ui.pushButton_4.clicked.connect(self.reset)
        self.ui.pushButton_2.clicked.connect(self.set_user_choice)
        self.ui.pushButton_3.clicked.connect(self.set_user_choice)
        self.user_choice = None
        self.computer1_choice = None
        self.computer2_choice = None
        self.user_total = 0
        self.computer1_total = 0
        self.computer2_total = 0
        self.round = 0
        self.flag = True

    def get_computer_choice(self):
        return random.choice(['🤚', '✋'])

    def set_user_choice(self):
      if self.flag == True:
        if self.sender() == self.ui.pushButton:
            self.user_choice = "✋"
        elif self.sender() == self.ui.pushButton_2:
            self.user_choice = "🤚"
        self.user_score, self.computer1_score, self.computer2_score = self.play_round()
        self.round +=1
        self.ui.textEdit_5.setText(f"Round: {self.round}")
        self.user_total += self.user_score
        self.computer1_total += self.computer1_score
        self.computer2_total += self.computer2_score

        self.ui.textEdit_2.setText(f"score: {self.user_total}")
        self.ui.textEdit_3.setText(f"score: {self.computer1_total}")
        self.ui.textEdit_4.setText(f"score: {self.computer2_total}")


        if self.round == 5 :

            if self.user_total > self.computer1_total and self.user_total > self.computer2_total:
               self.ui.textEdit.setText("You are the winner!")
            elif self.computer1_total > self.user_total and self.computer1_total > self.computer2_total:
               self.ui.textEdit.setText("Computer 1 is the winner!")
            elif self.computer2_total > self.user_total and self.computer2_total > self.computer1_total:
               self.ui.textEdit.setText("Computer 2 is the winner!")
            else:
              if self.user_total == self.computer1_total:
                self.ui.textEdit.setText("User and Computer 1 are equal!")
              if self.user_total == self.computer2_total:
                self.ui.textEdit.setText("User and Computer 2 are equal!")
              if self.computer1_total == self.computer2_total:
                self.ui.textEdit.setText("Computer 1 and Computer 2 are equal!")

            self.flag = False

         



    def play_round(self):
        
        self.computer1_choice = self.get_computer_choice()
        self.computer2_choice = self.get_computer_choice()

        self.text = f"User: {self.user_choice}, Computer1: {self.computer1_choice}, Computer2: {self.computer2_choice}"
        self.ui.textEdit.setText(self.text)

        self.user_score = int(self.user_choice != self.computer1_choice and self.user_choice != self.computer2_choice) 
        self.computer1_score = int(self.computer1_choice != self.user_choice and self.computer1_choice != self.computer2_choice) 
        self.computer2_score = int(self.computer2_choice != self.user_choice and self.computer2_choice != self.computer1_choice ) 
        

        # Reset the user choice buttons to allow a new selection
        self.ui.pushButton.setAutoExclusive(False)
        self.ui.pushButton_2.setAutoExclusive(False)
        self.ui.pushButton.setChecked(False)
        self.ui.pushButton_2.setChecked(False)
        self.ui.pushButton.setAutoExclusive(True)
        self.ui.pushButton_2.setAutoExclusive(True)

        return self.user_score, self.computer1_score, self.computer2_score
        
    def reset(self): 
      self.user_choice = None 
      self.computer1_choice = None 
      self.computer2_choice = None 
      self.user_total = 0 
      self.computer1_total = 0 
      self.computer2_total = 0 
      self.round = 0 
      self.ui.textEdit.setText("") 
      self.ui.textEdit_2.setText("score: 0") 
      self.ui.textEdit_3.setText("score: 0") 
      self.ui.textEdit_4.setText("score: 0") 
      self.ui.textEdit_5.setText("Round: 0")

    def about(self):
       msg_box= QMessageBox(text= "It is a Game which the User plays with 2 computers and should selects 🤚 or ✋, if the user_choice is not equal other 2 players, gets 1 score. After 5 round player who gets high scores win!! 🎉✨ ")
       msg_box.exec()

app = QApplication(sys.argv) 
main_window = MainWindow()
main_window.show()
app.exec()


