# implement equation in this link https://www.1728.org/cubic2.htm 

import math

def findF(a, b, c):
    F = ((3 * c / a) - ((b ** 2) / (a ** 2))) / 3
    return F


def findG(a, b, c, d):
    G = (((2 * (b ** 3)) / (a ** 3)) - ((9 * b * c) / (a **2)) + (27 * d / a)) /27
    return G


def findH(g, f):
    H = ((g ** 2) / 4 + (f ** 3) / 27)
    return H



def calculate_cubic(a, b, c, d):

    result = []

    if (a == 0 and b == 0):                 
                      
       x1 = (-d * 1) / c
       print("root is %.2f " %(x1))

    elif (a == 0):                              

        Delta = c * c - 4 * b * d                      
        if Delta >= 0:
            Delta = math.sqrt(Delta)
            x1 = (-c + Delta) / (2 * b)
            x2 = (-c - Delta) / (2 * b)
            print("Two equal and real roots are %.2f and %.2f" %(x1, x2))

        else:
            x1 = x2 = -b / (2 * a)
            i = math.sqrt(-Delta) / (2 * a)
            print("Two distinct complex roots are %.2f+%.2f and %.2f-%.2f"  %(x1, i, x2, i))
                  
        

    f = findF(a, b, c)                          
    g = findG(a, b, c, d)                      
    h = findH(g, f)    

# All 3 Roots are Real and Equal
    if f == 0 and g == 0 and h == 0:            
        if (d / a) >= 0:
            x = (d / (1 * a)) ** (1 / 3) * -1
        else:
            x = (-d / (1 * a)) ** (1 / 3)
                   
        print("Three equal and real roots are %.2f and %.2f and %.2f" %(x, x, x))   



# All 3 roots are Real
    elif h <= 0:                            

        i = math.sqrt(((g ** 2) / 4) - h)   
        j = i ** (1 / 3)                      
        k = math.acos(-(g / (2 * i)))          
        L = j * -1                             
        M = math.cos(k / 3)                   
        N = math.sqrt(3) * math.sin(k / 3)    
        P = (b / (3 * a)) * -1                

        x1 = 2 * j * math.cos(k / 3) - (b / (3 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

                 
        print("Three real roots are %.2f and %.2f and %.2f" %(x1, x2, x3))   

# One Real Root and two Complex Roots
    elif h > 0:                                 
 
        R = -(g / 2) + math.sqrt(h)           
        if R >= 0:
            S = R ** (1 / 3)                  
        else:
            S = (-R) ** (1 / 3) * -1 

        T = -(g / 2) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3))                
        else:
            
            U = ((-T) ** (1 / 3)) * -1

        x1 = (S + U) - (b / (3 * a))
        x2 = -(S + U) / 2 - (b / (3 * a)) +  (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3 * a)) -  (S - U) * math.sqrt(3) * 0.5j

    
        print("One Real Root and two Complex Roots are %.2f and %.2f and %.2f" %(x1, x2, x3)) 

    print(result)



a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))
d = int(input('Enter the value of d: '))


calculate_cubic(a, b, c, d)