import os 
import gtts
import pyfiglet
from termcolor import colored

def read_from_file():
 
 filename="session8/translate.txt"

 try:
  global words_bank
  words_bank = []
  #read file
  f = open(filename , "r")
  temp = f.read().split("\n")
  #create dictionary
  for i in range (0,len(temp),2):
    my_dic = {"en": temp[i],"fa": temp[i+1]}
    words_bank.append(my_dic)

  f.close()

 except OSError as e:
   print("File " + filename + " is not available, please upload the file.")

def convert_text_to_voice(my_text):

  x = gtts.gTTS(my_text, lang="en", slow = False )
  return x

def translate_english_to_persian():
 
 user_text = input("Enter your english text:").lower()

 user_texts = user_text.split(".")
 out_put= "" 
 for sentence in user_texts:
    user_words = sentence.split(" ")
    for user_word in user_words:
     for word in words_bank:
        if user_word == word["en"]:
            out_put += word["fa"] + " "
            break
     else:
        out_put += user_word + " "
    out_put += "."
 print(out_put)
 x = convert_text_to_voice(out_put)
 x.save("session8/voice1.mp3")

def translate_persian_to_english():
 
 user_text = input("Enter your persian text:").lower()

 user_texts = user_text.split(".")
 out_put= " " 
 for sentence in user_texts:
    user_words = sentence.split(" ")
    for user_word in user_words:
     for word in words_bank:
        if user_word == word["fa"]:
            out_put += word["en"] + " "
            break
     else:
        out_put += user_word + " "
    out_put += "."
 print(out_put)
 x = convert_text_to_voice(out_put)
 x.save("session8/voice2.mp3")

def write_in_file():

 filename="session8/translate.txt"

 try:
   f = open(filename, 'a')
   first_word = input("Enter your english word:").lower()
   f.write("\n" + first_word)
   second_word = input("enter your persian word:").lower()
   f.write("\n" + second_word)

   f.close()

 except OSError as e:
   print("File " + filename + " is not available, please upload the file.")
 
def show_menu():
  print(colored(pyfiglet.figlet_format("\nWelcome To My Translator", font = "doom"), color="light_yellow"))
  print(colored("menu", color="light_cyan"))
  print("1_Translate English To Persian")
  print("2_Translate Persian To English")
  print("3_Add a New Word To Database")
  print("4_Exit")

def main():
 while True:

  read_from_file()
  show_menu()


  choice = int(input(colored("Enter your choice:", color="light_magenta")))
  if choice == 1 :
    translate_english_to_persian()
  elif choice == 2:
    translate_persian_to_english()
  elif choice == 3:
     write_in_file()
  elif choice == 4:
    exit(0)
    

main()