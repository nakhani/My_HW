#Dice_rolling program


import random

#list = []

random_play = int(input('How many Dice do you want to roll? '))
select = input('Enter start:')

for i in range(random_play):
  if select == 'start':
     random_number = random.randint(1, 6)
     #list.append(tasadofi_number)
     print('taken number:', random_number)
     if random_number == 6:
        random_number = random.randint(1, 6)
        #list.append(tasadofi_number)
        print('reward:', random_number)
  else:
     print('please write start')
     break

     
#print(list)
   
