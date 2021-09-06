import pyttsx3

engine = pyttsx3.init()
#Control the rate. Higher rate = more speed
engine.setProperty("rate", 150)
text = "Hola mundo. Visita la USAC"
engine.say(text)
"""
Queue another audio
"""
another_text = "I like python"
engine.say(another_text)
engine.runAndWait()

