def is_symmetrical(arr):
    return arr == arr[::-1]

def check_symmetry():
    arr = []
    user_input = input("Enter a list of numbers separated by commas like 1,2,... : ")
    #arr = [int(item) for item in user_input.split(',')]
    items = user_input.split(',') 
    for item in items:
        arr.append(int(item))
    
    if is_symmetrical(arr):
        print("The array is symmetrical.")
    else:
        print("The array is not symmetrical.")

check_symmetry()