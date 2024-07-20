
import pyfiglet 
from termcolor import colored
from media import Media         
from dataset import Dataset
from product import Product

db=Dataset("My_HW/session12/database.txt")
def show():
    print(colored("_____________________________________________________\n",color="light_grey"))
    print(colored("Menu:", color="light_cyan"))
    print("1_Add")
    print("2_Edit")
    print("3_Remove")
    print("4_Search")
    print("5_show List")
    print("6_Exit\n")

def main():
 title = colored(pyfiglet.figlet_format("StellaMovie", font = "doom"), color="light_yellow")
 print(title)
 print(colored("Loading...",color="light_green"))
 db.read()
 print(colored("Data Loaded...",color="light_red"))


 while True:
  show()
  choice = int(input(colored("Enter your choice:", color="light_magenta")))

  if choice == 1 :
        Product.add()
  elif choice == 2:
        Product.edit()
  elif choice == 3:
        Product.remove()
  elif choice == 4:
        Product.search()
  elif choice == 5:
        Product.showlist()
  elif choice == 6:
        db.write()
        exit(0)
         
  else:
        print(colored("Please select number in range 1 to 6", color="light_red"))

main()
