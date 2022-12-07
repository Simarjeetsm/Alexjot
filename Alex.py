import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
# from bs4 import BeautifulSoup
# import requests

engine = pyttsx3.init('sapi5')
rate = engine.getProperty("rate")
engine.setProperty("rate", 140)

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

    speak("sat shri aakaal, Mai Alexjot Kaur waa , Poch ki pushhna ")
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



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open Linkedin' in query:
            webbrowser.open("LinkedIn.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'bol time' in query:
            speak(f"Mai Tere Pao di naukar nahi waa")


       #Detects downloaded music and plays it
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'please time bol' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"suun la time kaan khol ke {strTime} vaa")


        #Opens python code editor
        # elif 'python' in query:
        #     codePath = "C:\\Users\\simar\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
        #     os.startfile(codePath)
            
            
        # elif "temperature" in query:
            
        #     search = "temperature in jorhat"
        #     url = f"https://www.google.com/search?q={search}"
        #     r = requests.get(url)
        #     data = BeautifulSoup(r.text, "html parser")
        #     temp = data. find("div" "class_""Bleave").text
        #     speak(f"current {search} is {temp}")



