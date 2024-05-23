


side1 = int(input('please choose your first side: '))
side2 = int(input('please choose your second side: '))
side3 = int(input('please choose your third side: '))

if side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1:
    print('this triangle can draw')
else:
    print('this triangle can not draw')