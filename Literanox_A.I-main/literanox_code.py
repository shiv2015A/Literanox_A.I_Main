import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import pyjokes
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import webbrowser
from playsound import playsound
import winshell
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil

from bs4 import BeautifulSoup
import pywhatkit
import os

os.system('color 02')







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    #engine.say()
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening!") 
  
    assname =("literanox")
    speak("I am your Assistant")
    speak(assname)


    speak("What should i call you ")
    uname = takeCommand()


    
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
    speak("How can i Help you")
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





if __name__ == "__main__":
    
    wishMe()
    while True:
        
        query = takeCommand().lower()
       
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To wikipedia")
            print(results)
            speak(results)



            
        elif 'open youtube'  in query:
            webbrowser.open("youtube.com")

            
            
            

        elif "open google"  in query:
            webbrowser.open("www.google.com")



        elif "set an alarm" in query:
            speak("What time should I set an alarm for")
            time = takeCommand(": What time should Iset an alarm for :")


            #while True:
                #Time_Ac = datetime.datetime.now()
                #now = Time_Ac.
          

        elif 'play chand baliya' in query:
            webbrowser.open("https://www.youtube.com/watch?v=7c3-Gei5j4w")
            
        elif 'play despacito' in query:
            webbrowser.open("https://www.youtube.com/watch?v=whwe0KD_rGw")

        elif 'play sad' in query:
            webbrowser.open("https://www.youtube.com/watch?v=TQM3LuK0tG4&t=1541s")

        elif 'play kishore kumar hits' in query:
            webbrowser.open("https://www.youtube.com/watch?v=tUWrm3tkbKQ")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H %M %S")
            speak(f"Sir, the time is{strTime}")

        elif 'yash veer favourite song' in query:
            webbrowser.open("https://youtu.be/m_1ieZfGwks")
            
        



        elif 'how are you' in query:
            speak("I am fine, how are you?")

        elif "what is your name" in query:
            speak("My friends call me literanox")
            
            print("My friends call me literanox")

        elif 'i am feeling bored' in query:
            speak(' you should try doing something interesting and if u dont have something Interesting, you should consider studying something This will also help you in ur academics!')


        elif 'what is perimeter of rectangle' in query:
            speak('Perimeter of rectangle = 2 into (length+width)')

        elif 'what is perimeter of square' in query:
            speak('perimeter of square = 4 into side') 

        elif 'what is area of rectangle' in  query:
            speak ('area of rectangle = length into breadth')

        elif 'what is area of square' in query:
            speak('area of square = side into side')

        elif 'hello' in query:
            speak('hello , how are you')

        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif 'tell me a story' in query:
            speak('A Stag had fallen sick. He had just strength enough to gather some food and find a quiet clearing in the woods, where he lay down to wait until his strength should return. The Animals heard about the Stags illness and came to ask after his health. Of course, they were all hungry, and helped themselves freely to the Stags food; and as you would expect, the Stag soon starved to death ,   moral of the story is Good will is worth nothing unless it is accompanied by good acts')

        elif 'where do you live' in query:
            speak('i am not a living being hence i can not live but i occupy some space or memory in your device so that can be where i live')


        elif 'tell me about yourself' in query:
            speak ('i am litranox, your personal assistant you can ask me several questions and i will answer those for you')

        elif 'bye' in query:
            speak("bye, Thanks for giving me your time")
            exit()

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        
        elif 'what can you do' in query:
            speak("i can open youtube, google, play several songs, tell you the time, tell you the weather i can also tell you jokes! and manymore")

        elif "temperature" in query:
            search = "temprature in ara"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div" ,class_="BNeawe").text
            speak(f"current{search} is {temp}")


        elif "can you do maths" in query:
            speak("yes, i can do simple maths, here is the calculator enter the digits")
            filePath = "2# Python program for simple calculator.py"
            os.startfile(filePath)

        elif "first mission of isro" in query:
            speak("The Aryabhata spacecraft, named after the famous Indian astronomer, was India's first satellite; it was completely designed and fabricated in India and launched by a Soviet Kosmos-3M rocket from Kapustin Yar on April 19, 1975")



        elif 'play' in query:
            s = "opening youtube"
            engine.say(s)
            engine.runAndWait()
            pywhatkit.playonyt(query)


        #elif "search" in query:
            #a = "searching"
            #engine.say(a)
            #engine.runAndWait()
            #pywhatkit.search(query)

        elif "search" in query:
            import wikipedia as googleScrap
            query = query.replace("literanox","")
            query = query.replace("search","")
            query = query.replace("google","")
            speak("this is what i found on the web!")

            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("Data can Not be processed!")
            
        
        elif 'algo expert' in query:
            webbrowser.open("algoexpert.io")


        elif 'square root' in query:
            filePath = "3# Python Program to calculate the square.py"
            os.startfile(filePath)

        elif 'profit and loss' in query:
            filePath = "Profit loss calculator.py"
            os.startfile(filePath)

        elif 'kilometer to miles' in query:
            filePath = "4# Python Program to convert kilometer to miles.py"
            os.startfile(filePath)

        elif 'rectangle' in query:
            filePath = "1# Area _ Perimeter of Rectangle.py"

        elif 'square'  in query:
            filePath = "3# Python Program to calculate the square.py"
            os.startfile(filePath)

        elif 'triangle' in query:
            filePath = '10#Perimeter = s1 + s2 + s3py.r'
            os.startfile(filePath)


        elif 'circle' in query:
            filePath = "5# Python Program to find Diameter, Circu.py"
            os.startfile(filePath)

        elif 'sphere' in query:
            filePath = "8# Python Program to find Volume and Surf.py"
            os.startfile(filePath)

        elif 'cube' in query:
            filePath = "7# Python Program to find Volume and Surf sphere.py"

        elif 'cuboid' in query:
            filePath = "6# Python Program to find Volume and Surf of cuboid.py"







 
    


        

        

 # Made by Shivansh Dubey
                                   

