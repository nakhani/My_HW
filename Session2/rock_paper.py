#Rock_paper_scissor game


import random


computer_score = 0
user_score = 0
num = random.randint(1, 3)


#while True:
for i in range(4):

   if num == 1:
      computer_choice = 'rock'
   elif num == 2:
      computer_choice = 'paper'
   if num == 3:
      computer_choice = 'scissor'

   user_choice = input(('please choose rock, paper, scissor:'))

   if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissor':
      print('computer_choice:', computer_choice)
      print('user_choice:', user_choice)

      if computer_choice == 'rock' and user_choice == 'paper':
           user_score += 1

      elif computer_choice == 'rock' and user_choice == 'scissor':
           computer_score += 1

      elif computer_choice == 'paper' and user_choice == 'rock':
           computer_score += 1

      elif computer_choice == 'paper' and user_choice == 'scissor':
           user_score += 1

      elif computer_choice == 'scissor' and user_choice == 'paper':
          computer_score += 1

      elif computer_choice == 'scissor' and user_choice == 'rock':
          user_score += 1

      print('computer_score:', computer_score)
      print('user_score:', user_score)

   else:
        print('input is not correct')


   #elif user_choice == 'exit':
   #   break

   


