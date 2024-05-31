import qrcode
import pyfiglet 
from termcolor import colored

def read_from_database():
  global PRODUCTS

  PRODUCTS = []
  f = open("session7\database.txt", "r")


  for line in f :

    result = line.split(",")
    my_dic = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
    PRODUCTS.append(my_dic)

  f.close()


def sub_edit(a,b):
  print(colored("_____________________________________________________\n",color="light_grey"))
  code = input("Enter Product CODE:")
  
  for product in PRODUCTS:
         if product[a]== code:
            if b == "name":
             new_name = input("Enter New Name:")
             product[b] = new_name
             print(colored("Edit Done successfully", color="light_green"),"✔")
             print (colored (product,color="light_yellow"))
            elif b == "price":
             new_name = input("Enter New Price:")
             product[b] = new_name
             print(colored("Edit Done successfully", color="light_green"),"✔")
             print (colored (product,color="light_yellow"))
            elif b == "count":
             new_name = input("Enter New Count:")
             product[b] = new_name
             print(colored("Edit Done successfully", color="light_green"),"✔")
             print (colored (product,color="light_yellow"))
            break
  else:
         print(colored("Not Found\n",color="yellow"))

def edit():
  while True:
    print(colored("_____________________________________________________\n",color="light_grey"))
    print(colored("What part of data do you want to Edit?", color="light_cyan"))
    print("1_Edit Name")
    print("2_Edit Price")
    print("3_Edit Count")
    print("4_exit")

    choice = int(input(colored("Enter your choice:", color="light_magenta")))

    if choice == 1 :

     sub_edit("code","name")
    
    elif choice == 2:

     sub_edit("code","price")

    elif choice == 3:

     sub_edit("code","count")
    
    elif choice == 4:
       break


def QR_CODE():
  print(colored("_____________________________________________________\n",color="light_grey"))
  code = input("Enter Product CODE:")
  for product in PRODUCTS:
    if (product["code"] == code):
      code1 = product["code"]
      name = product["name"]
      price= product["price"]
 
      qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
      
      qr.add_data("code: "+code1+"\n"+"name: "+name+"\n"+"price: "+price)

      qr.make(fit=True)
      img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
      img.save("user_qrcode.png")
      print(colored("QR_CODE is created successfully", color="light_green"), "✔\n")
      break
  else:
    print(colored("Not Found\n",color="light_red"))


def buy():
  print(colored("_____________________________________________________\n",color="light_grey"))
  list = []
  count = 0
  while True:
    code = input("Enter Product CODE:")
    for product in PRODUCTS:
       if product["code"] == code:
         a = int( product["count"])
         num = int(input(colored("How many do you want?",color="light_magenta")))
         if num >= a:
           print("we have just:", product["count"])
           break
         elif num == a or num < a :
           product["count"] = a - num
           cost = int(product["price"]) * num
           b = {"code": product["code"], "name": product["name"],"number": num,"price":cost}
           list.append(b)
           break
       else:
          print(colored("Not Found\n",color="light_red")) 
    
    conti = input("Do you want to continue?Y/N  ").lower()
    if conti == "n": 
        break
#factor
  print (colored("code \t\t name \t\t number \t price", color="yellow"))
  for product in list:
    print (product["code"], "\t\t", product["name"], "\t\t", product["number"], "\t\t", product["price"])
    c = int(product["price"])
    count += c
  print("-----------------------------------------")
  print("total_cost: ", count, "\n\n")
  print(colored("Do you want pay?",color="light_magenta"))

      
       


def add():
    
    print(colored("_____________________________________________________\n",color="light_grey"))
    code = input("Enter code:")
    name = input("Enter name:")
    price = input("Enter price:")
    count = input("Enter count:")
    new_product = {"code": code, "name": name, "price": price, "count": count}
    PRODUCTS.append(new_product)
    print(colored("New Product was added successfully", color="light_green"), "✔")


def write_to_database():

   f = open(f"session7\database.txt", "w")
   for product in PRODUCTS:
     f.write(product["code"]+ ","+ product["name"]+","+product["price"]+","+product["count"])
   print(colored("_____________________________________________________\n",color="light_grey"))
   print(colored("update done", color="light_green"), "✔")
   f.close()


def remove():
  print(colored("_____________________________________________________\n",color="light_grey"))
  code = input("Enter Product CODE:")

  for product in PRODUCTS:
    if product["code"]== code:
      PRODUCTS.remove(product)
      print(colored("Delete Done", color="light_green"), "✔")
      break
  else:
    print(colored("Not Found\n",color="light_red"))

  
    

def search():
  print(colored("_____________________________________________________\n",color="light_grey"))
  user_input = input("Enter Product CODE or NAME:")
  for product in PRODUCTS:
      if product["code"] == user_input or product["name"] == user_input:
         print(colored("Your search result is:", color="light_blue"))
         print(colored("code\tname\tprice", color="light_yellow"))
         print(product["code"], "\t", product["name"], "\t", product["price"])
         break
  else:
      print(colored("Not Found\n",color="light_red"))


def show_list():
   print(colored("_____________________________________________________\n",color="light_grey"))
   print(colored("code\tname\tprice", color="light_yellow"))
   for product in PRODUCTS:
    print(product["code"], "\t", product["name"], "\t", product["price"])


def show():
    print(colored("_____________________________________________________\n",color="light_grey"))
    print(colored("Menu:", color="light_cyan"))
    print("1_Add")
    print("2_Edit")
    print("3_Remove")
    print("4_Search")
    print("5_show List")
    print("6_Buy")
    print("7_QR-CODE")
    print("8_Exit\n")


def main():
 title = colored(pyfiglet.figlet_format("StellaStore", font = "doom"), color="light_yellow")
 print(title)
 print(colored("Loading...",color="light_green"))
 read_from_database()
 print(colored("Data Loaded...",color="light_red"))


 while True:
  show()
  choice = int(input(colored("Enter your choice:", color="light_magenta")))

  if choice == 1 :
        add()
  elif choice == 2:
        edit()
  elif choice == 3:
        remove()
  elif choice == 4:
        search()
  elif choice == 5:
        show_list()
  elif choice == 6:
        buy()
  elif choice == 7:
        QR_CODE()
  elif choice == 8:
         write_to_database()
         exit(0)
  else:
        print(colored("Please select number in range 1 to 7", color="light_red"))

main()
