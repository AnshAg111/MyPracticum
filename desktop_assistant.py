import streamlit as st
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import threading
from backend import Chatbot

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!" + "I am Jarvis, Sir. Please tell me how may I help you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!" + "I am Jarvis, Sir. Please tell me how may I help you")
    else:
        speak("Good Evening!" + "I am Jarvis, Sir. Please tell me how may I help you")
    speak("I am Jarvis, Sir. Please tell me how may I help you")
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

def jarvis():
    # wishMe()
    while True:
        query = takecommand().lower()
        # print(query)
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print("hello"+results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'data structure' in query or 'coding' in query:
            webbrowser.open("leetcode.com")
        elif 'google classroom' in query:
            webbrowser.open("classroom.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open("jiosaavn.com")
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        elif 'open code' in query:
            path = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'search for me' in query:
            webbrowser.open("google.com/search?q="+query.replace("search for me ", ''))
        elif 'quit' in query:
            speak('Quitting')
            break
        else:
            chatbot=Chatbot()
            response=chatbot.get_response(query)
            speak(response)
    

# if __name__ == '__main__':
st.title('Hi, this is your AI desktop assistant. Ask anything you want!')
button_clicked = st.button('Click me to start Jarvis')
if button_clicked:
    wishMe()
    jarvis()
        
        
