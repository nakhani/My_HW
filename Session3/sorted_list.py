#Sort List and check

numlist1 = []

num = int(input("Please enter the Total Number of List Elements: "))

if num == 1:
      print("your list just have 1  element")


else:
   for i in range(1, num + 1):
     value = int(input("Please enter the Value of %d Element : " %i))
     numlist1.append(value)

   def checksortedlist (newlist):
     isSorted = True
     for i in range(len(newlist)- 1):
        if newlist[i] > newlist[i + 1]:
            isSorted = False
     return isSorted


   def sortlist(newlist):
     for i in range (len(newlist)):
        for j in range(i + 1, len(newlist)):
          if(newlist[i] > newlist[j]):
             temp = numlist1[i]
             newlist[i] = newlist[j]
             newlist[j] = temp
     return newlist


   result = checksortedlist(numlist1)
   if result == False:
    sortlist(numlist1)
    print("your sorted_list is:", numlist1)
   else:
    print("your list was sorted")
