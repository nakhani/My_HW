# removing duplicates from the list using naive methods 


numlist1 = []
result = []

list1 = int(input("Please enter the Total Number of List Elements: "))


if list1 == 1:
      print("your list just have 1  element")

else:
   for i in range(1, list1 + 1):
     value = int(input("Please enter the Value of %d Element : " %i))
     numlist1.append(value)

for i in numlist1: 

  if i not in result: 
   result.append(i) 

print ("The list after removing duplicates : " + str(result))