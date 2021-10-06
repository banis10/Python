import pyttsx3
import speech_recognition as sr

s = True
while s == True:
    engine = pyttsx3.init()
    #Control the rate. Higher rate = more speed
    engine.setProperty("rate", 150)
    text = "Buen dia, por favor coloque su DPI"
    engine.say(text)
    engine.runAndWait()
    #detectar DPI

    k = True
    while k == True:
        text = '¿Para qué tipo de vacuna viene?, Moderna, Astrazeneca, Sputnik o Faiser'
        engine.say(text)
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Por favor diga su respuesta')
            audio = r.listen(source)
            try:
                rec = r.recognize_google(audio, language = 'es-ES')
                vac = rec.split()
                print('respuesta = : {}'.format(rec))
                print(vac)
                if 'moderna' in vac:
                    print('respuesta = : {}'.format(rec))
                    vac1 = "Viene para la vacuna Moderna"
                    engine.say(vac1)
                    engine.runAndWait()
                    vacuna = 'Moderna'
                    k = False
                elif 'astrazeneca' in vac:
                    print('Su vacuna es : {}'.format(rec))
                    vac2 = "Viene para la vacuna Astrazeneca"
                    engine.say(vac2)
                    engine.runAndWait()
                    vacuna = 'Astrazeneca'
                    k = False
                elif 'sputnik' in vac:
                    print('respuesta = : {}'.format(rec))
                    vac3 = "Viene para la vacuna Sputnik"
                    engine.say(vac3)
                    engine.runAndWait()
                    vacuna = 'SputnikV'
                    k = False
                elif 'pfizer'in vac:
                    print('respuesta = : {}'.format(rec))
                    vac4 = "Viene para la vacuna Pfizer"
                    engine.say(vac4)
                    engine.runAndWait()
                    vacuna = 'Pfizer'
                    k = False
                else:
                    print('respuesta = : {}'.format(rec))
                    vac5 = "Por favor repita su respuesta"
                    engine.say(vac5)
                    engine.runAndWait()
            except:
                text3 = "Por favor repita"
                engine.say(text3)
                engine.runAndWait()

    n = True
    while n == True:
        text = "¿Viene para la primera, o segunda dosis?"
        engine.say(text)
        engine.runAndWait()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
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
                    dosis = 'Primera'
                    n = False
                elif 'segunda' in vac:
                    text2 = "Viene a la segunda dosis, por favor dirijase al módulo, B"
                    engine.say(text2)
                    engine.runAndWait()
                    dosis = 'Segunda'
                    n = False
                else:
                    text3 = "Por favor repita su respuesta"
                    engine.say(text3)
                    engine.runAndWait()
            except:
                text3 = "Por favor repita su respuesta"
                engine.say(text3)
                engine.runAndWait()
                print('Por favor repita su respuesta')

    print(vacuna, dosis)
