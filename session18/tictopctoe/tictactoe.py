from functools import partial
import random
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader 

winner = False
count = 0


def check_game():
    global winner
    winner = True
    #check row and col
    for x in range (0, 3):
        if (buttons[x][0].text() == buttons[x][1].text() == buttons[x][2].text() == "X" or
         buttons[0][x].text() == buttons[1][x].text() == buttons[2][x].text() == "X"):
            winner = False
        elif (buttons[x][0].text() == buttons[x][1].text() == buttons[x][2].text() == "O" or 
        buttons[0][x].text() == buttons[1][x].text() == buttons[2][x].text() == "O" ):
            winner = False
            break

    # Check the diagnoals   
    if (buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() == "X" or
     buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text() == "X"):
        winner = False 
    elif (buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() == "O" or
     buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text() == "O"):
        winner = False
    
    return winner

def mood(x):
   
   if x==1:
      return x
   elif x==2:
      return x


def play(row, col,x):
    global player, count,winner
    global change_mood
    if player == 1:
          buttons[row][col].setText("X")
          buttons[row][col].setStyleSheet("color:lightblue; background-color:white;")
          player= 2
    count+=1
    if count>2:
     winner = check_game()
     if winner == False: 
       msg_box= QMessageBox(text= "Player 1 won")
       msg_box.exec()
       
    if x == "player2":   
        if player == 2:
          buttons[row][col].setText("O")
          buttons[row][col].setStyleSheet("color:white; background-color:lightblue;")
          player = 1
    elif x == "CPU":
       row = random.randint(0, 2)
       col = random.randint(0,2)
       while buttons[row][col].text() != "":
          row = random.randint(0, 2)
          col = random.randint(0,2)
       buttons[row][col].setText("O")
       buttons[row][col].setStyleSheet("color:white; background-color:lightblue;")
       player = 1

    if count>2:
      winner = check_game()
      if winner == False:
        if x == "player2":
            msg_box= QMessageBox(text= "Player 2 won")
            msg_box.exec()
        elif x == "CPU":
            msg_box= QMessageBox(text= "computer won")
            msg_box.exec()
    if winner == True:
            msg_box= QMessageBox(text= "there is no winner")
            msg_box.exec()
def mode(x):
  for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play,i,j,x))

def about():
   
  msg_box= QMessageBox(text= "This is a TicTocToe Game")
  msg_box.exec()


def reset():
   for i in range(3):
    for j in range(3):
        buttons[i][j].setText("")
        buttons[i][j].setStyleSheet("background-color: rgb(255, 169, 224);")

   main_window.btn_C.setText(" C(CPU):")
   main_window.btn_Ties.setText(" TIES:")
   main_window.btn_X.setText(" X(YOU):")


loader = QUiLoader()
app = QApplication([])
player = 1

main_window = loader.load("tictoctoe\main.ui")
main_window.show()


buttons= [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
         [main_window.btn_4, main_window.btn_5, main_window.btn_6],
         [main_window.btn_7, main_window.btn_8, main_window.btn_9]]



#x = "CPU" if main_window.rbtn_1.isChecked() else  "player2"

main_window.btn_about.clicked.connect(about)
main_window.btn_reset.clicked.connect(reset)
main_window.rbtn_1.clicked.connect(partial(mode, "CPU"))
main_window.rbtn_2.clicked.connect(partial(mode,"player2"))
app.exec()