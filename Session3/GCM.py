#GCM


num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

#method1

#while num1 != num2:
#    if num1 > num2:
#        num1 -= num2
#    else:
#        num2 -= num1

#print("GCM is:", num1)

#method 2

def GCM (a, b):
  if a > b:
    min1 = b
  else:
    min1 = a
  for i in range (1 , min1+1):
     if(a % i == 0 and b % i == 0):
        gcm = i
  return gcm

result = GCM (num1,num2)
print("GCM is:", result)
