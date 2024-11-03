#random_list

import random

def rand(row,col, start_range, end_range):
  random_list =[]
  index = 0
  
  total_number = row*col
  if end_range - start_range +1 <total_number :
     raise ValueError ("Not enough unique numbers in the given range")
  
  unique_numbers = random.sample(range(start_range,end_range+1),total_number)
  
  for i in range (row):
    num1 = []
    for j in range (col):
       num1.append(unique_numbers[index])
       index += 1 
    random_list.append(num1)

  return(random_list)

