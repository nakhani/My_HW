class number:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    

    def dev (self):
        ...
    def sub (self):
        ...
    def sum (self):
        ...
    def conv (self):
        ...
    def mult (self):
        ...
    def frac (self):
        ...


def show_menu():
  print("1_division")
  print("2_sum")
  print("3_subtraction")
  print("4_multiplication")
  print("5_fraction number")
  print("6_conventionalize")
  print("7_exit")


def main():
  n1 = int(input("please enter nm1 of first fraction:"))
  n2 = int(input("please enter nm2 of first fraction:"))
  n3 = int(input("please enter nm1 of second fraction:"))
  n4 = int(input("please enter nm2 of second fraction:"))

  if n2 == 0 or n4 == 0 :
    print("your fraction undefined")

  else: 
   action = number(n1, n2, n3, n4)
   while True:
    show_menu()

    choice = int(input("enter your choice:"))
    if choice == 1 :
     result = action.dev
    elif choice == 2:
     result = action.sum
    elif choice == 3:
     result = action.sub
    elif choice == 4:
     result = action.mult
    elif choice == 5:
     result = action.com
    elif choice == 6:
     exit()

    print (result)
