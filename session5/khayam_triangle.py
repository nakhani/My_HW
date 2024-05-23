#print khayam_pascal_traingle

from math import factorial


m = int(input("please enter number:"))


def traingle(rows):
	for i in range(rows):
          for j in range(i+1):
        # nCr = n!/((n-r)!*r!)
             print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

          print()

traingle(m)