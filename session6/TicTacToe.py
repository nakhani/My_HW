import pyfiglet 
from termcolor import colored
import time
import random

winner = False
count = 0
#show game_board
def show():
    for row in game_board:
      for cell in row:
        if cell == "X":
          print(colored(cell,"blue"), end= " ") 
        elif cell == "O":
          print(colored(cell, "red"), end= " ") 
        else:
          print(cell, end= " ") 
      print()
    print("\n") 
#check winner
def check_game():
    winner = True
    #check row and col
    for x in range (0, 3):
        if (game_board[x][0] == game_board[x][1] == game_board[x][2] == "X" or
         game_board[0][x] == game_board[1][x] == game_board[2][x] == "X"):
            winner = False
        elif (game_board[x][0] == game_board[x][1] == game_board[x][2] == "O" or 
        game_board[0][x] == game_board[1][x] == game_board[2][x] == "O" ):
            winner = False
            break

    # Check the diagnoals   
    if (game_board[0][0] == game_board[1][1] == game_board[2][2] == "X" or
     game_board[0][2] == game_board[1][1] == game_board[2][0] == "X"):
        winner = False 
    elif (game_board[0][0] == game_board[1][1] == game_board[2][2] == "O" or
     game_board[0][2] == game_board[1][1] == game_board[2][0] == "O"):
        winner = False
    
    return winner
    
#start
title = pyfiglet.figlet_format("TicTacToe", font = "5lineoblique")
print(title)
#select player
user_selected = int(input("please select\n 2 for play player1 with player2 \n 1 for play player1 with computer:"))

game_board = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]

show()
start = time.time()

#total loop
while count < 5:
#player 1
  print("player1")
  while True:
    row = int(input("row:"))
    col = int(input("col:"))
    if 0 <= row <= 2 and 0 <= col <= 2 :
      if game_board[row][col] == "_":
         game_board [row][col] = "X"
         break
      else:
         print("please select another row and col")
    else:
        print("please select another row and col nmber")
  show()
  count += 1
  if count>2:
    winner = check_game()
    if winner == False: 
     print("player 1  you won!")
     break
#player2 and computer
  while count < 5:
    if user_selected == 2:
      print("player 2")
      row = int(input("row:"))
      col = int(input("col:"))
      if 0 <= row <= 2 and 0 <= col <= 2 :
        if game_board[row][col] == "_":
         game_board [row][col] = "O"
         break
        else:
         print("please select another row and col")
      else:
        print("please select another row and col nmber")
    elif user_selected == 1:
        print("computer")
        row = random.randint(0,2)
        col = random.randint(0,2)
        if 0 <= row <= 2 and 0 <= col <= 2 :
          if game_board[row][col] == "_":
           game_board [row][col] = "O"
           break
  show()
  if count>2:
    winner = check_game()
    if winner == False:
        if user_selected == 2:
                print("Player 2 you won!")
        elif user_selected == 1:
                print("computer you won!")
        break
#end
end = time.time() - start
#check if neither of player won
if winner == True:
    print("There is not winner")

print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(end)))
