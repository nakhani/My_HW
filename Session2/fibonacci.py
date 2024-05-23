#Fibonacci program


num = int(input('How many terms the user wants to print? '))

def fibonacci_of(n):
  if n in {0, 1}:  
   return n

  return fibonacci_of(n - 1) + fibonacci_of(n - 2)  

list = []
#[fibonacci_of(n) for n in range(num)]
for n in range(num):
    result = fibonacci_of(n)
    list.append(result)
    #print(result)

print(list)
 