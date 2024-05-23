from statistics import mean



name = input('please enter your first name and last name: ')

first_course = float(input('enter your first course: '))
second_course = float(input('enter your second course: '))
third_course = float(input('enter your third course: '))

list = [first_course, second_course, third_course]


def additonal (n):
   s= 0
   for x in n:
    s = s + x
   return(s)

result = additonal (list)
result = result / len (list)

#result = sum(list)
#result = result / len(list)

#result = mean (list)

#print (result)

if result >= 17:
    print('Great student')
elif  result >= 12 and result < 17:
    print('Normal student')
elif result < 12:
    print('Fail student')

