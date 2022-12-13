import qrcode


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
  code = input("Enter Product CODE:")
  
  for product in PRODUCTS:
         if product[a]== code:
            new_name = input("Enter New Name:")
            product[b] = new_name
            print("Edit Done sucessfully\n")
            print (product)

            break
  else:
         print("Not Found\n")

def edit():
  while True:

    print("1_Edit Name")
    print("2_Edit Price")
    print("3_Edit Count")
    print("4_exit")

    choice = int(input("enter your choice:"))

    if choice == 1 :

     sub_edit("code","name")
    
    elif choice == 2:

     sub_edit("code","price")

    elif choice == 3:

     sub_edit("code","count")
    
    elif choice == 4:
       break


def QR_CODE():

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

      qr.make(fit = True)
      img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
      img.save("user_qrcode.png")
      print("QR_CODE creat successful\n")
      break
  else:
    print("Not Found\n")


def buy():
  list = []
  count = 0
  while True:
    code = input("Enter Product CODE:")
    for product in PRODUCTS:
       if product["code"] == code:
         a = int( product["count"])
         num = int(input("How many do you want?"))
         if num >= a:
           print("we have just:", product["count"])
         elif num == a or num < a :
           product["count"] = a - num
           cost = int(product["price"]) * num
           b = {"code": product["code"], "name": product["name"],"number": num,"price":cost}
           list.append(b)
           break
    else:
        print("Not Found") 
    
    conti = input("Do you want to continue?Y/N  ").lower()
    if conti == "n" or "N": 
      break
#factor
  print ("code \t\t name \t\t number \t price")
  for product in list:
    print (product["code"], "\t\t", product["name"], "\t\t", product["number"], "\t\t", product["price"])
    c = int(product["price"])
    count += c
  print("-----------------------------------------")
  print("total_cost: ", count, "\n\n")
  print("Do you want pay?")

      
       


def add():

    code = input("enter code:")
    name = input("enter name:")
    price = input("enter price:")
    count = input("enter count:")
    new_product = {"code": code, "name": name, "price": price, "count": count}
    PRODUCTS.append(new_product)


def write_to_database():

   f = open(f"session7\database.txt", "w")
   for product in PRODUCTS:
     f.write(product["code"]+ ","+ product["name"]+","+product["price"]+","+product["count"])

   print("update done")
   f.close()


def remove():
  
  code = input("Enter Product CODE:")

  for product in PRODUCTS:
    if product["code"]== code:
      PRODUCTS.remove(product)
     
      break
  else:
    print("Not Found")

  print("Delete Done")
    

def search():
  user_input = input("enter code")
  for product in PRODUCTS:
      if product["code"] == user_input or product["name"] == user_input:
         print(product["code"], "\t", product["name"], "\t", product["price"])
         break
  else:
      print("Not Found")


def show_list():
   print("code\t\tname\t\tprice")
   for product in PRODUCTS:
    print(product["code"], "\t", product["name"], "\t", product["price"])


def show():

    print("1_Add")
    print("2_Edit")
    print("3_Remove")
    print("4_Search")
    print("5_show List")
    print("6_Buy")
    print("7_QR-CODE")
    print("8_Exit")


def main():

 print("Welcom to Stella Store")
 print("Loading...")
 read_from_database()
 print("Data Loaded.")


 while True:
  show()
  choice = int(input("enter your choice:"))

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
        print("please select number in range 1 to 7")

main()
