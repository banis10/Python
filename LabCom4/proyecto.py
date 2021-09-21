import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
#Control the rate. Higher rate = more speed
engine.setProperty("rate", 150)
text = "Buenos dias, para que dosis de vacuna viene"
engine.say(text)
"""
Queue another audio
"""
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say something...')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language = 'es-ES')
        print('What did you say : {}'.format(text))
    except:
        print('Sorry! I can\'t understand')
        

text1 = "Viene a la primera dosis, por favor dirijase al módulo A"
engine.say(text1)
"""
Queue another audio
"""
engine.runAndWait()
text2 = "Viene a la segunda dosis, por favor dirijase al módulo B"
engine.say(text2)
"""
Queue another audio
"""
engine.runAndWait()
