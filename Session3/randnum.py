#random_list

import random

n = int(input("How many number do you want to generate?:"))
random_list =[]

for i in range (n):

    num1 = random.randint(0,100)

    if num1 not in random_list:
        random_list.append(num1)

print(random_list)