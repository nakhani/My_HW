# my_first_calculator 

from cmath import pi
import math
from math import radians 


print('Welcome to this calculator!')
print('It can add, subtract, multiply, divide, sin, cos, cot, tan, sqrt, factorial')
sign = input('What do you want to do? +, -, /, *, sin, cos, tan, cot, sqrt, factorial: ')

lists = ['+' , '-' , '/' , '*']

#if sign == '+' or sign == '-' or sign == '*' or sign == '/':
if sign in lists:
   num1 = float(input('Please choose your first number: '))
   num2 = float(input('Please choose your second number: '))
else:
   num1 = float(input('Please choose your first number: '))


if sign == '+':
   result = num1 + num2
elif sign == '-':
   result = num1 - num2
elif sign == '/':
   if num2 == 0:
      result = 'can not devide'
   else:
      result = num1 / num2
elif sign == '*':
      result = num1 * num2
elif sign == 'sin':
      #num1 = num1 / (math.pi * 180)  
      num1 = radians (num1)
      result = math.sin(num1)   
elif sign == 'cos':
      num1 = radians (num1)
      result = math.cos(num1)  
elif sign == 'cot':
      num1 = radians (num1)
      result = math.atan(num1) 
elif sign == 'tan':
      num1 = radians (num1)
      result = math.tan(num1) 
elif sign == 'sqrt':
   if num1 < 0:
      print('input is not correct')
   else:
      result = num1 ** 0.5
   #result = math.sqrt(num1)
elif sign == 'factorial':
   factorial = 1    
   if num1 < 0:    
      print(" Factorial does not exist for negative numbers")    
   elif num1 == 0:    
      print("The factorial of 0 is 1")    
   else:    
      for i in range(1,num1 + 1):    
         factorial = factorial*i    
         result = factorial
   #result = math.factorial(num1)

print(result)        
      
