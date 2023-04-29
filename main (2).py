from PyQt6.QtWidgets import * # QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot
# from main import jarvis
import threading
#import speech_recognition as sr
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

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
            speak("Good Morning!")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon")
        else:
            speak("Good Evening!")
        speak("I am Jarvis, Sir. Please tell me how may I help you")

def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            # print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            # print(f"User said: {query}\n")
        except Exception as e:
            # print(e)
            speak("Say that again please...")
            return "None"
        return query
    
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Robo speaker")
        self.chatbot=Chatbot()
        self.setMinimumSize(700, 500)
        self.chat_area=QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 1500, 600)
        self.chat_area.append("<h1>Hi, this is your AI desktop assistant. Ask anything you want!</h1>")
        self.chat_area.setReadOnly(True)
        # self.input_field=QLineEdit(self)
        # self.input_field.setGeometry(10, 720, 1000, 100)
        # self.input_field.returnPressed.connect(self.send_message)
        self.button=QPushButton("Ask Something", self)
        self.button.setGeometry(675, 640, 150, 50)
        self.button.clicked.connect(self.send_message)
        self.show()
        
    def send_message(self):
        wishMe()
        query = takecommand().lower()
        self.chat_area.append(f"<p style='color:#333333'>Me: {query}</p>")
        if 'wikipedia' in query:
                self.chat_area.append("<p style='color:#333333; background-color: #E9E9E9'>Bot: Searching wikipedia... </P>")
                speak('Searching wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                # print(results)
                speak(results)
        elif 'open youtube' in query:
                self.chat_area.append("<p style='color:#333333; background-color: #E9E9E9'>Bot: opening youtube... </P>")
                webbrowser.open("youtube.com")
                
        elif 'open google' in query:
                self.chat_area.append("<p style='color:#333333; background-color: #E9E9E9'>Bot: opening google... </P>")
                webbrowser.open("google.com")
        elif 'data structure' in query or 'coding' in query:
                self.chat_area.append("<p style='color:#333333; background-color: #E9E9E9'>Bot: opening leetcode... </P>")
                webbrowser.open("leetcode.com")
        elif 'google classroom' in query:
                self.chat_area.append("<p style='color:#333333; background-color: #E9E9E9'>Bot: opening google classroom</P>")
                webbrowser.open("classroom.google.com")
        elif 'open stackoverflow' in query:
                self.chat_area.append("<p style='color:#333333; background-color: #E9E9E9'>Bot: opening stackoverflow... </P>")
                webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
                webbrowser.open("jiosaavn.com")
        elif 'the time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: Sir, the time is {strtime}</P>")
                speak(f"Sir, the time is {strtime}")
        elif 'open code' in query:
                path = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
        elif 'search for me' in query:
                self.chat_area.append("<p style='color:#333333; background-color: #E9E9E9'>Bot: Searching... </P>")
                webbrowser.open("google.com/search?q="+query.replace("search for me ", ''))
        else:
            # user_input=self.input_field.text().strip()
            # print(user_input)
            
            # self.input_field.clear()
            
            thread=threading.Thread(target=self.get_bot_response, args=(query, ))
            thread.start()
        
        
    def get_bot_response(self, user_input):
        response=self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</P>")
        speak(response)
        

app=QApplication(sys.argv)
main_window=ChatbotWindow()
sys.exit(app.exec())