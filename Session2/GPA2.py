#Calculate GPA


from statistics import mean

name = input('please enter your first name and last name: ')
list = []

while True:
    course = input('enter your scores course: ')
    several = course.isdigit()
    if course == 'exit':
        break
    elif course == 'avg':
        #avg = sum(list) / len(list)
        avg = mean (list)
        print ('your average :',avg)
    else:
        score = float(course)
        list.append(score)

    #avg = mean (list)
    #print ('your average is:',avg)








