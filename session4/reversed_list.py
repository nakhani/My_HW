
#method1

# def Reverse(lst):
#     new_lst = lst[::-1]
#     return new_lst


numlist1 = [] 

list1 = int(input("Please enter the Total Number of List Elements: "))


if list1 == 1:
      print("your list just have 1  element")

else:
   for i in range(1, list1 + 1):
     value = int(input("Please enter the Value of %d Element : " %i))
     numlist1.append(value)

# print(Reverse(numlist1))

#method2
new_list = [numlist1[len(numlist1) - i]
            for i in range(1, len(numlist1)+1)]
print(new_list)
