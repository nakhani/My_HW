#Convert hour, minute and second into second


hour = int(input("Input hours: ")) * 3600
minute = int(input("Input minutes: ")) * 60
second = int(input("Input seconds: "))

#h, m, s = int(input("Input hours, minute, second: "))

second = hour + minute + second

print("The  amounts of seconds", second)


