import pyttsx3

def talk():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate - 50)
    engine.say('Hello and welcome to LANGUAGE TRANSLATOR IN PYTHON')
    engine.say('This system gives a facility to translate any language to any language')
    engine.say('Now enter the input and output language code to proceed further')
    engine.runAndWait()