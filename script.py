from types import CodeType
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os, sys, subprocess 

engine=pyttsx3.init()
voices=engine.getProperty("voices")
#print(type(voices))
#for i in range(0,len(voices)):
#    print(voices[i].id, i)
engine.setProperty('voice', voices[11].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("Hi I am your assistant")    

def takeCommand():
    # it take microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please ...")
        return "None"
    return query

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia ...')
            query = query.replace("wikipedia", "") if query != "wikipedia" and len(query.split()) != 2 else query
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("Opening Youtube ...")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Opening Google ...")
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = "/home/subham/Music/"
            songs = os.listdir(music_dir)
            speak("Playing a song")
            open_file(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {time_str}")
            speak(f"The time is {time_str}")

        elif "open code" in query:
            codePath = "/usr/bin/code"
            speak("Opening VS code")
            os.system(codePath)
