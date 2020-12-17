from gtts import gTTS 
import os 
language = 'en'
hello = input("Enter text to speech word")
mytext=hello
myobj = gTTS(text=mytext, lang=language, slow=True)
myobj.save("voice.mp3") 
os.system("mpg321 mycomd.mp3")

