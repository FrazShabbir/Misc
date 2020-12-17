from gtts import gTTS 
import os 
import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=15)
    print("Recognizing...")
    # convert speech to text using api
    text = r.recognize_google(audio_data)
    print(text)
    language = 'en'
    mytext=text
    myobj = gTTS(text=mytext, lang=language, slow=True) 
    myobj.save("mycomd.mp3") 
    os.system("mpg321 mycomd.mp3")