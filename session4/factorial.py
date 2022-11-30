
num1 = int(input('Please choose your first number: '))

def inverse_fact(input):
    n = 1
    i = 1
    while True:
        if input % i == 0: # If divided without remainder
            n*= i
            if n == input:
                return i
        else:
            return 0
        i += 1

result = inverse_fact(num1)
if result == 0:
      print("NO")
else:
      print("Yes")


