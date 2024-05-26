#Calculate GPA


from statistics import mean

def show():
    print("you can choose: 1. GPA  2.continue  3.exit")

def avg(m):
    gpa= mean (m)
    print ("your average : %.2f" %(gpa))

name = input('please enter your first name and last name: ')
list = []
while True:
    show()
    course = input("enter your choice: ")
    if course == 'exit':
        avg(list)
        break
    elif course == 'GPA':
        avg(list) 
        break         
    elif course == 'continue':
         score = float(input("enter your score: "))
         list.append(score)








