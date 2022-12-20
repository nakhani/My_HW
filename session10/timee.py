class timeee:

    def __init__(self):
        self.hour1 = None
        self.minute1 = None
        self.second1 = None
        self.hour2 = None
        self.minute2 = None
        self.second2 = None
       


    def conv_to_other_times (self,hour1,minute1,second1):
        ...
    def differance (self,hour1,minute1,second1,hour2,minute2,second2):
        ...
    def convert_to_second (self,hour1,minute1,second1):
        ...
    def convert_to_hour (self,second1):
        ...


def show_menu():
  print("1_convert to other times")
  print("2_calculate diference")
  print("3_convert to second")
  print("4_convert to hour")
  print("5_exit")


def main():
 
  while True:

    show_menu()
    choice = int(input("enter your choice:"))
    if choice == 1 :
      hour1 = int(input("enter hour:"))
      minute1 = int(input("enter minute:"))
      second1 = int(input("enter second:"))
      result = timeee.conv_to_other_times(hour1,minute1,second1)
    elif choice == 2:
      hour1 = int(input("enter first hour:"))
      minute1 = int(input("enter first minute:"))
      second1 = int(input("enter first second:"))
      hour2 = int(input("enter second hour:"))
      minute2 = int(input("enter second minute:"))
      second2 = int(input("enter second second:"))
      result = timeee.differance(hour1,minute1,second1,hour2,minute2,second2)
    elif choice == 3:
      hour1 = int(input("enter hour:"))
      minute1 = int(input("enter minute:"))
      second1 = int(input("enter second:"))
      result = timeee.convert_to_second(hour1,minute1,second1)
    elif choice == 4:
      second1 = int(input("enter second:"))
      result = timeee.convert_to_second(second1)
    elif choice == 6:
     exit()

    print (result)
