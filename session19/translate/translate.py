

def read_from_file():
 
 filename="translate/translate.txt"

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


def translate_english_to_persian(x):
 
 user_text = x.lower()

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
 return out_put

def translate_persian_to_english(x):
 
 user_text = x.lower()

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
 return out_put




read_from_file()
    

