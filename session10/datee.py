class datee:

    def __init__(self):
        self.year1 = None
        self.month1 = None
        self.day1 = None
        self.year2 = None
        self.month2 = None
        self.day2 = None
       


    def conv_to_other_dates (self,ye1,mon1,day1):
        ...
    def difference (self,ye1,mon1,day1,ye2,mon2,day2):
        ...
    def convert_to_day (self,ye1,mon1,day1):
        ...
    def convert_to_year (self,day1):
        ...
    def cal_age (self,ye1,mon1,day1):
        ...


def show_menu():
  print("1_convert to other dates")
  print("2_calculate difference")
  print("3_convert to day")
  print("4_convert to year")
  print("5_calculate age")
  print("6_exit")


def main():
 
  while True:

    show_menu()
    choice = int(input("enter your choice:"))
    if choice == 1 :
      year = int(input("enter year:"))
      month = int(input("enter month:"))
      day = int(input("enter day:"))
      result = datee.conv_to_other_dates(year,month,day)
    elif choice == 2:
      year = int(input("enter first year:"))
      month = int(input("enter first month:"))
      day = int(input("enter first day:"))
      year2 = int(input("enter second year:"))
      month2 = int(input("enter second month:"))
      day2 = int(input("enter second day:"))
      result = datee.difference(year,month,day,year2,month2,day2)
    elif choice == 3:
      year = int(input("enter year:"))
      month = int(input("enter month:"))
      day = int(input("enter day:"))
      result = datee.convert_to_day(year,month,day)
    elif choice == 4:
      day = int(input("enter day:"))
      result = datee.convert_to_year(day)
    elif choice == 5:
      year = int(input("enter year:"))
      month = int(input("enter month:"))
      day = int(input("enter day:"))
      result = datee.cal_age(year,month,day)
    elif choice == 6:
     exit()

    print (result)
