#Guess_play program


import random

computer_number = random.randint(10, 40)
counter = 0
#counter = 1

for i in range (10, 40):
   user_number = int(input('Enter your guess number:'))

   if computer_number == user_number:
      print('you win')
      break

   elif computer_number > user_number :
      print('go up')

   elif computer_number <= user_number :
      print('go down')

   counter += 1
   

print('you win after:', counter)
