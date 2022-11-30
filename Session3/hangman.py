#hangman play


import random


words_bank = ["ali", "tree", "pink", "fashion", "flower", "free", "language", "bag", "dress"]
user_mistake = 0

good_chars = []
bad_chars = []


x = random.randint(0, len(words_bank)-1)
#print(x)
word = words_bank[x]

while user_mistake < 6:
   flag=1

   for i in range (len(word)):
     if word[i] in good_chars:
        print(word[i], end="")

     else:
        flag = 0
        print("- ", end="" )

   if flag == 1:
      print("\n\nyou win")
      break

   user_char = input("  please write your guess:")
   user_char = user_char.lower()

   if len(user_char) == 1:

     if user_char in word:
       good_chars.append(user_char)
       print("true")

     else:
        bad_chars.append(user_char)
        user_mistake +=1
        print("false")

   else:
      print("please enter one character")

   

if user_mistake == 6:
      print("\nGame over")


