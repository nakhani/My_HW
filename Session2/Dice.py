#Dice_rolling program


import random

def check_dice ():
        m = random.randint(1, 6)
        return(m)

select = input('Enter start:')     
if select == 'start':
      number=check_dice()
      print('taken number:', number)
      while number == 6:
         number=check_dice()
         print('your reward is:', number)
else:
     print('please write start')
     
   
