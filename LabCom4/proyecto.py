import pyttsx3
import speech_recognition as sr
import time
engine = pyttsx3.init()
#Control the rate. Higher rate = more speed
engine.setProperty("rate", 150)
text = "Buenos dias,por favor coloque su DPI"
engine.say(text)
engine.runAndWait()
text = "Para que dosis de vacuna viene"
engine.say(text)
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    print('Por favor diga su respuesta')
    audio = r.listen(source)
    try:
        rec = r.recognize_google(audio, language = 'es-ES')
        print('Su respuesta es : {}'.format(rec))
        vac = rec.split()
        print(vac)
        if 'primera' in vac:
            text1 = "Viene a la primera dosis, por favor dirijase al módulo, A"
            engine.say(text1)
            engine.runAndWait()
        elif 'segunda' in vac:
            text2 = "Viene a la segunda dosis, por favor dirijase al módulo, B"
            engine.say(text2)
            engine.runAndWait()
        else:
            text3 = "Por favor repita su respuesta"
            engine.say(text3)
            engine.runAndWait()
    except:
        text3 = "Por favor repita su respuesta"
        engine.say(text3)
        engine.runAndWait()
        print('Por favor repita su respuesta')
        

# vac = rec.split()
# print(vac)

# if 'primera' in vac:
    # text1 = "Viene a la primera dosis, por favor dirijase al módulo, A"
    # engine.say(text1)
    # engine.runAndWait()
# elif 'segunda' in vac:
    # text2 = "Viene a la segunda dosis, por favor dirijase al módulo, B"
    # engine.say(text2)
    # engine.runAndWait()
# else:
    # text3 = "Por favor repita su respuesta"
    # engine.say(text3)
    # engine.runAndWait()

