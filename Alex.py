import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from bs4 import BeautifulSoup
import requests


chrome_path=r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(chrome_path))

engine = pyttsx3.init('sapi5')
rate = engine.getProperty("rate")
engine.setProperty("rate", 135)

#engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("  sat shri aakaal, Mai Alexjot Kaur waa , Poch ki pushhna ")
    # speak(" Iam zira, how can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif 'time bol de' in query:
            speak(f" Tere Paeo di naukar nahi waa, aappe dekh la")
            
            

        elif 'youtube khol' in query:
            webbrowser.get('chrome').open("youtube.com")
        elif 'Linkedin khol' in query:
            webbrowser.get('chrome').open("LinkedIn.com")
        elif 'google khol' in query:
            webbrowser.get('chrome').open("google.com")
        elif 'stacko verflow khol' in query:
            webbrowser.get('chrome').open("stackoverflow.com")
            
        elif 'kida wa' in query:
            speak(f"Baas wadia apana suna")
        


       #Detects downloaded music and plays it
        elif 'songs waja' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'please time bol' in query:
            strTime = datetime.datetime.now().strftime("%I:%M")
            speak(f"suun la time kaan khol ke {strTime} vaa")


        #Opens python code editor
        elif 'python khol' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1\\bin\\pycharm64.exe"
            os.startfile(codePath)
            
        elif 'vs code khol' in query:
            codePath = "C:\\Users\\simar\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
            
            
            
        elif "temperature" in query:
            
            search = "temperature in jorhat"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html parser")
            temp = data. find("div" "class_""Bleave").text
            speak(f"current {search} is {temp}")


