
import math

def calculate_eq(a, b, c): 
    
    Delta = (b**2) - (4*a*c)

    if(Delta > 0):
        x1 = (-b + math.sqrt(Delta) / (2 * a))
        x2 = (-b - math.sqrt(Delta) / (2 * a))
        print("Two distinct real roots are %.2f and %.2f" %(x1, x2))

    elif(Delta == 0):
        x1 = x2 = -b / (2 * a)
        print("Two equal and real roots are %.2f and %.2f" %(x1, x2))

    elif(Delta < 0):
        x1 = x2 = -b / (2 * a)
        i = math.sqrt(-Delta) / (2 * a)
        print("Two distinct complex roots are %.2f+%.2f and %.2f-%.2f"  %(x1, i, x2, i))


a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))


calculate_eq(a, b, c)