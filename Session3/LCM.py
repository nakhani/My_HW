#LCM


num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))


#Method1

#if(num1>num2):
#    max=num1
#else:
#    max=num2
#while(1):
#    if(max%num1==0 and max%num2==0):
#        print("LCM is:",max)
#        break
#    max=max+1

#Method2

def LCM (a,b):
  for i in range (max(a,b), (a*b)+1):
     if(i%a==0 and i%b==0):
       return i

result = LCM (num1,num2)
print("LCM is:", result)

    