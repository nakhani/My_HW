import gtts

my_text="i am najmeh a python programmer"

x = gtts.gTTS(my_text, lang="en", slow = False )
x.save("session8/voice.mp3")