#print multiply_table

rows = int(input("please enter row's number:"))
columns = int(input("please enter column's number:"))

def multiply (n,m):
  for row in range(1,n+1):
    for col in range(1,m+1):
        print(row*col,end = " ")
    print()

multiply(rows, columns)

