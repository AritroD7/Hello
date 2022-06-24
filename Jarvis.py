from datetime import datetime
import pyttsx3
import speech_recognition as sr
import datetime




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Goodmorning boss!")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon boss!")
        
    else:
        speak("Good evening boss!")
    speak("How can I help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ ==  "__main__":
    wishMe()
    takeCommand()
    