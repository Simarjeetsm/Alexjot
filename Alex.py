import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

chrome_path=r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(chrome_path))

engine = pyttsx3.init('sapi5')
rate = engine.getProperty("rate")
engine.setProperty("rate", 135)

#engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[3].id)

# for voice in voices:
#     print(voice.id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#   Uses to wish according to 

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
        r.pause_threshold = 0.5
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
            speak(f" Tere Paeo di naukar nahi waa, aappe dekh la annea")
            
            

        elif 'youtube khol' in query:
            webbrowser.get('chrome').open("youtube.com")
        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")
            
        elif 'Linkedin khol' in query:
            webbrowser.get('chrome').open("linkedin.com")
        elif 'open Linkedin' in query:
            webbrowser.get('chrome').open("linkedin.com")
            
        elif 'stack overflow khol' in query:
            webbrowser.get('chrome').open("stackoverflow.com")
        elif 'open stack overflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")
            
        elif 'twitter khol' in query:
            webbrowser.get('chrome').open("twitter.com")
        elif 'open twitter' in query:
            webbrowser.get('chrome').open("twitter.com")
            
        elif 'hello' in query:
             speak(f"chal chal , apna kaam kar daammag naa khaa")
        


       #Detects downloaded music and plays it
        elif 'gane' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
            

        elif 'please time bol' in query:
            strTime = datetime.datetime.now().strftime("%I:%M")
            speak(f"suun la time kaan khol ke {strTime} vaa")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        #Opens python code editor
        elif 'python khol' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1\\bin\\pycharm64.exe"
            os.startfile(codePath)
            
        elif 'vs code khol' in query:
            codePath = "C:\\Users\\simar\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)


