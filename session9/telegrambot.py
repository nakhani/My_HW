
import random
import telebot
import gtts
import qrcode
from khayyam import JalaliDate, JalaliDatetime 

bot = telebot.TeleBot("Your Bot Token", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=7)
key_1 = telebot.types.KeyboardButton('/start')
key_2 = telebot.types.KeyboardButton('/help')
key_3 = telebot.types.KeyboardButton('/game')
key_4 = telebot.types.KeyboardButton('/age')
key_5 = telebot.types.KeyboardButton('/new-game')
key_6 = telebot.types.KeyboardButton('/text_to_voice')
key_7 = telebot.types.KeyboardButton('/max')
key_8 = telebot.types.KeyboardButton('/argmax')
key_9 = telebot.types.KeyboardButton('/qrcode')
markup.add(key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  user_first_name = str(message.chat.first_name) 
  bot.send_message(message.chat.id, f" Hi, {user_first_name}  \n\n Welcome To Najmeh Bot ", reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.send_message(message.chat.id, "you can send these commands to use me:\n\n"+ 
                          "/game or /new-game - play guess game\n"+ 
                          "/age - enter your birthdate to calculate your age\n"+
                          "/text_to_voice - convert your text to voice\n"+
                          "/max - print max number of your list\n"+
                          "/argmax - print max index of your list\n"+
                          "/qrcode - get qrcode of your list\n", reply_markup=markup)

@bot.message_handler(commands=['game', 'new-game'])
def game(message):
  global rnnum
  rnnum = random.randint(10, 40)
  bot.send_message(message.chat.id,"Welcome to 'Guess the Number' game. \n\nEnter a number between 0 and 40:")
  @bot.message_handler(func=lambda m: True)
  def guess(message):
            usernumber = int(message.text)
            if usernumber == rnnum:
                bot.send_message(message.chat.id, "Congratulations! you won.", reply_markup=markup)
                bot.remove_message_handler(guess)
            elif usernumber < rnnum:
                bot.send_message(message.chat.id, "please go up.")
            else:
                bot.send_message(message.chat.id, "please go down.")

            bot.add_message_handler(guess)

@bot.message_handler(commands= ["age"])
def age(message):
  bot.send_message(message.chat.id, "Enter your date of birth (yy/mm/dd):")
  @bot.message_handler(func=lambda m: True)
  def calculage(message):
     userbirdate = message.text
     userbirdate = userbirdate.split("/")
     differ = JalaliDatetime.now() - JalaliDatetime(userbirdate[0], userbirdate[1], userbirdate[2])
     year = differ.days // 365
     differ = differ.days % 365
     month = differ // 30
     day = differ % 30 - 7
     result= "your age: " + str(year) + " years and " + str(month) + " months and " + str(day) + " days"
     bot.send_message(message.chat.id, result, reply_markup=markup)

@bot.message_handler(commands= ["text_to_voice"])
def text_to_voice(message):
  bot.send_message(message.chat.id, "Enter your Text: ")
  @bot.message_handler(func=lambda m: True)
  def convert(message):
    usertext= message.text
    x = gtts.gTTS(usertext, lang="en", slow = False )
    # x.save("/content/drive/MyDrive/VoiceBot.mp3")
    # voice = open("/content/drive/MyDrive/VoiceBot.mp3", 'rb')
    x.save("VoiceBot.mp3")
    voice = open("session9\VoiceBot.mp3", 'rb')
    bot.send_audio(message.chat.id, voice, reply_markup=markup)

@bot.message_handler(commands= ["max"])
def innum(message):
  bot.send_message(message.chat.id,"Please Enter numbers with comma.\n(forexample: 2,3,4,1,7,0 = 7)")
  @bot.message_handler(func=lambda m: True)
  def calculmax(message):
    text = message.text
    newarray = text.split("," or "," or ", " or " " or " ,")
    max = 0
    for num in newarray:
      if max < int(num):
        max = int(num)
    bot.send_message(message.chat.id, f"The maximum number is {max}", reply_markup=markup)

@bot.message_handler(commands= ["argmax"])
def innum(message):
  bot.send_message(message.chat.id,"Please Enter numbers with comma.\n(forexample: 2,3,4,1,7,0 = 7)")
  @bot.message_handler(func=lambda m: True)
  def calculargmax(message):
    text = message.text
    newarray = text.split("," or "," or ", " or " " or " ,")
    max = 0
    i= 0
    for num in newarray:
      if max < int(num):
        max = int(num)
        index = i
      i=i+1
    bot.send_message(message.chat.id, f"The argmax  is {index}", reply_markup=markup)

@bot.message_handler(commands= ["qrcode"])
def instr(message):
  bot.send_message(message.chat.id,"Please Enter your text: ")
  @bot.message_handler(func=lambda m: True)
  def qr(message):
    text = message.text
    img = qrcode.make(text)
    # img.save("/content/drive/MyDrive/qrcode.png")
    # newimg = open("/content/drive/MyDrive/qrcode.png","rb")
    img.save("qrcode.png")
    newimg = open("session9\qrcode.png","rb")
    bot.send_photo(message.chat.id, newimg, reply_markup=markup)

# from google.colab import drive
# drive.mount('/content/drive')

bot.infinity_polling()