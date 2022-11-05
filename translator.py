import googletrans

import speech_recognition as sr

import gtts

import playsound


print("\n\n")

print("###### WELCOME TO LANGUAGE TRANSLATOR IN PYTHON ######".center(155))

print("      ------------------------------------------".center(150))

recognizer = sr.Recognizer()
translator = googletrans.Translator()

print("\n\n")
print(" * Let us now see the available languages for various translations : \n")

print(googletrans.LANGUAGES)
print("\n\n")



print(" * Now let us enter the input and output language codes for further communication : ")
print()

i = input('Enter code of input language : ')
j = input('Enter code of output language : ')
print()


#talk('Speak Now')

try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=i)
        print(text)


except:
    pass


translated = translator.translate(text, dest=j)
print(translated.text)


converted_audio = gtts.gTTS(translated.text, lang=j)

converted_audio.save('eng.mp3')

playsound.playsound('eng.mp3')




