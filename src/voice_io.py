import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id) 
    engine.setProperty('rate', 160)  
    engine.say(text)
    engine.runAndWait()
    




def voice():
    r = sr.Recognizer()
    listen = True
    while listen:
        try:
            with sr.Microphone() as source:
                print('Listening....')
                audio = r.listen(source , timeout=3 )
                print('Recognizing....')
                query = r.recognize_google(audio , language='en-in')
                print(f'You Said : {query}')
                listen = False
        except Exception as e:
            speak(''' Sorry Couldn't Understand Can you Please Try Again ''')

            
    return query.lower()

    
# DONE.........