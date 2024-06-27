def carpet(n):
    if n % 2 == 0:
        print("Please enter an odd number.")
        return
    outer_symbol = "🌸"
    middle_symbol1 = "🟣"
    middle_symbol2 = "🔵"
    middle_symbol3 = "🟤"
    middle_symbol4 = "🟡"
    middle_symbol5 = "🟠"

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print(outer_symbol, end=' ')
            elif i == 1 or i == n-2 or j == 1 or j == n-2:
                print(middle_symbol1, end=' ')
            elif i == 2 or i == n-3 or j == 2 or j == n-3:
                print(middle_symbol2, end=' ')
            elif i == 3 or i == n-4 or j == 3 or j == n-4:
                print(middle_symbol3, end=' ')
            elif i == 4 or i == n-5 or j == 4 or j == n-5:
                print(middle_symbol5, end=' ')
            elif i == (n//2) and j == (n//2):
                print(middle_symbol4, end=' ')
            else:
                print(middle_symbol3, end=' ')
        print()

number = int(input("Enter your number: "))
carpet(number)
