import gtts

my_text="happiness is when your code runs without errors"

x = gtts.gTTS(my_text, lang="en", slow = False )
x.save("session8/voice.mp3")