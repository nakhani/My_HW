class Timeee:

    def __init__(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
     
       


    def conv_to_other_times (self,ho1,min1,sec1):
        ...
    def difference (self,ho1,min1,sec1,ho2,min2,sec2):
        ...
    def convert_to_second (self,ho1,min1,sec1):
        ...
    def convert_to_hour (self,sec1):
        ...
    def fix(self):
      if self.second >= 60:
        self.second -= 60
        self.minute += 1

      if self.minute >= 60:
        self.minute-= 60
        self.hour += 1

      if self.minute < 0:
        self.minute += 60
        self.hour -= 1

      if self.second < 0:
        self.second += 60
        self.minute -= 1

def show_menu():
  print("1_convert to other times")
  print("2_calculate difference")
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
      result = Timeee.conv_to_other_times(hour1,minute1,second1)
    elif choice == 2:
      hour1 = int(input("enter first hour:"))
      minute1 = int(input("enter first minute:"))
      second1 = int(input("enter first second:"))
      hour2 = int(input("enter second hour:"))
      minute2 = int(input("enter second minute:"))
      second2 = int(input("enter second second:"))
      result = Timeee.differance(hour1,minute1,second1,hour2,minute2,second2)
    elif choice == 3:
      hour1 = int(input("enter hour:"))
      minute1 = int(input("enter minute:"))
      second1 = int(input("enter second:"))
      result = Timeee.convert_to_second(hour1,minute1,second1)
    elif choice == 4:
      second1 = int(input("enter second:"))
      result = Timeee.convert_to_second(second1)
    elif choice == 6:
     exit()

    print (result)
