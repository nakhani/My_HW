#count words


string = input("Please enter your string: ")

count_words = 0
check_space = 0

for i in range(len(string)):
   if string[i] == " ":
      if check_space != 0:
        count_words += 1
      check_space = 0
   else:
        check_space += 1
if check_space != 0:
    count_words += 1

print("number of words in your string is:", count_words)     
