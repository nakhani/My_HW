import qrcode
import pyfiglet 
from termcolor import colored
import sqlite3

def read_from_database():
    global con, my_cursor, PRODUCTS

    con = sqlite3.connect("sql_store/store.db")
    my_cursor = con.cursor()
    result = my_cursor.execute("SELECT * FROM products")
    PRODUCTS = result.fetchall()

def sub_edit(a, b):
    print(colored("_____________________________________________________\n", color="light_grey"))

    code = int(input("Enter Product CODE:"))

    for product in PRODUCTS:
        if product[0] == code:  
            if b == "name":
                new_value = input("Enter New Name:")
                my_cursor.execute(f"UPDATE products SET name = '{new_value}' WHERE id = '{code}'")
            elif b == "price":
                new_value = float(input("Enter New Price:"))
                my_cursor.execute(f"UPDATE products SET price = '{new_value}' WHERE id = '{code}'")
            elif b == "count":
                new_value = int(input("Enter New Count:"))
                my_cursor.execute(f"UPDATE products SET count = '{new_value}' WHERE id = '{code}'")
            
            con.commit()
            print(colored("Edit Done successfully", color="light_green"), "✔")
            print(colored(product, color="light_yellow"))
            break
    else:
        print(colored("Not Found\n", color="yellow"))

def edit():
    while True:
        print(colored("_____________________________________________________\n", color="light_grey"))
        print(colored("What part of data do you want to Edit?", color="light_cyan"))
        print("1_Edit Name")
        print("2_Edit Price")
        print("3_Edit Count")
        print("4_exit")

        choice = int(input(colored("Enter your choice:", color="light_magenta")))

        if choice == 1:
            sub_edit(0, "name")  
        elif choice == 2:
            sub_edit(0, "price")  
        elif choice == 3:
            sub_edit(0, "count")  
        elif choice == 4:
            break

def QR_CODE():
    print(colored("_____________________________________________________\n", color="light_grey"))
    code = int(input("Enter Product CODE:"))
    for product in PRODUCTS:
        if product[0] == code:  
            code1 = product[0]
            name = product[1]
            price = product[2]

            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(f"code: {code1}\nname: {name}\nprice: {price}")
            qr.make(fit=True)
            img = qr.make_image(fill_color='red', back_color='white')
            img.save("user_qrcode.png")
            print(colored("QR_CODE is created successfully", color="light_green"), "✔\n")
            break
    else:
        print(colored("Not Found\n", color="light_red"))

def buy():
    print(colored("_____________________________________________________\n", color="light_grey"))
    purchase_list = []
    total_cost = 0
    while True:
        code = int(input("Enter Product CODE:"))
        for product in PRODUCTS:
            if product[0] == code:  
                available_count = product[3]  
                num = int(input(colored("How many do you want?", color="light_magenta")))
                if num > available_count:
                    print(f"We have just: {available_count}")
                    break
                else:
                    new_count = available_count - num
                    my_cursor.execute(f"UPDATE products SET count = '{new_count}' WHERE id = '{code}'")
                    con.commit()
                    cost = product[2] * num
                    purchase_list.append((product[0], product[1], num, cost))
                    break
        else:
            print(colored("Not Found\n", color="light_red"))

        conti = input("Do you want to continue? (Y/N): ").lower()
        if conti == "n":
            break

    # factor
    print(colored("code \t\t name \t\t number \t price", color="yellow"))
    for item in purchase_list:
        print(item[0], "\t\t", item[1], "\t\t", item[2], "\t\t", item[3])
        total_cost += item[3]
    print("-----------------------------------------")
    print("total_cost: ", total_cost, "\n\n")
    print(colored("Do you want to pay?", color="light_magenta"))

def add():
    print(colored("_____________________________________________________\n", color="light_grey"))
    code = int(input("Enter code:"))
    name = input("Enter name:")
    price = float(input("Enter price:"))
    count = int(input("Enter count:"))
    my_cursor.execute(f"INSERT INTO products (id, name, price, count) VALUES ('{code}', '{name}', '{price}', '{count}')")
    con.commit()
    print(colored("New Product was added successfully", color="light_green"), "✔")

def remove():
    print(colored("_____________________________________________________\n", color="light_grey"))
    code = int(input("Enter Product CODE:"))
    my_cursor.execute(f"DELETE FROM products WHERE id = '{code}'")
    con.commit()
    print(colored("Delete Done", color="light_green"), "✔")

def search():
    print(colored("_____________________________________________________\n", color="light_grey"))
    user_input = input("Enter Product CODE or NAME:")
    for product in PRODUCTS:
        if str(product[0]) == user_input or product[1].lower() == user_input.lower():
            print(colored("Your search result is:", color="light_blue"))
            print(colored("code\tname\tprice", color="light_yellow"))
            print(product[0], "\t", product[1], "\t", product[2])
            break
    else:
        print(colored("Not Found\n", color="light_red"))

def show_list():
    print(colored("_____________________________________________________\n", color="light_grey"))
    print(colored("code\tname\tprice", color="light_yellow"))
    for product in PRODUCTS:
        print(product[0], "\t", product[1], "\t", product[2])

def show():
    print(colored("_____________________________________________________\n", color="light_grey"))
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
    title = colored(pyfiglet.figlet_format("StellaStore", font="doom"), color="light_yellow")
    print(title)
    print(colored("Loading...", color="light_green"))
    read_from_database()
    print(colored("Data Loaded...", color="light_red"))

    while True:
        show()
        choice = int(input(colored("Enter your choice:", color="light_magenta")))

        if choice == 1:
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
            con.close()
            exit(0)
        else:
            print(colored("Please select number in range 1 to 7", color="light_red"))

main()
