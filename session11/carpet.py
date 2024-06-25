import random
list=["🎀","🌸","☘","🍁","🍂","🌼","🌻","🌺","🍄","🌴"]
      
def carpet(n):
    for i in range (1, n):
        for j in range (1, n):
         x= random.choice(list)
         print(x, end = " ")
        print()

        
number=int(input("Please enter your number?"))

if number%2==0 :
    print("This is just python Homework")

else:
    carpet(number)
    