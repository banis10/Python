import speech_recognition as sr 
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say something...')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es-ES")
        print('What did you say : {}'.format(text))
    except:
        print('Sorry! I can\'t understand') 