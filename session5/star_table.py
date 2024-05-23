#print star_table


rows = int(input("please enter row's number:"))
columns = int(input("please enter column's number:"))

def array (n,m):
   for row in range(1,n+1):
      print("#*", end = " ")
      for col in range(1,m):
        print("#*", end = " ")
      print()

array(rows, columns)