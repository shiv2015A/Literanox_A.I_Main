import speech_recognition as sr
import os
import pyttsx3
os.system('color 01')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # engine.say()
    engine.runAndWait()
speak(' Say wake up to initiate the main code!')


def takeCommand():
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
    assname =("literanox")
    speak("I am your Assistant")
    speak(assname)








while True:
    wake_Up = takeCommand()

    if 'wake up' in wake_Up:
      os.startfile("H:\Literanox_A.I-main\Literanox_A.I-main\literanox_code.py")
      exit()
    else:
        print("nothing...")

