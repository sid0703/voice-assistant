import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import random
import time
import pyjokes

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello Everyone. I am your Voice Assisstant. How may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Command: {query}\n")

    except Exception as e:

        print("Sorry can't hear you. Please say it again.")
        speak("Sorry can't hear you. Please say it again.")
        return "None"
    return query

def coin():
    toss = ['heads','tails']
    result = toss[random.randrange(0,1)]
    print(f"It's a {result}")
    speak(f"It's a {result}")

def close():
    exit()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia,")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("opening youtube")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            print("opening Google")
            speak("opening Google")
        
        elif 'toss a coin' in query:
            coin()

        elif 'notepad' in query:
            print("opening Notepad")
            speak("opening notepad")
            Note = 'C:\\Windows\\system32\\notepad.exe' #insert the path location according to ur system
            os.startfile(Note)
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f'The time now is{strTime}')

        elif 'spotify' in query:
            print("opening spotify")
            speak("opening spotify")
            spotify ="C:\\Users\\lakha\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify)

        elif 'roll a dice' in query:
            dice = ['1','2','3','4','5','6']
            num = random.choice(dice)
            print(f"the number is {num}")
            speak(f"the number is {num}")


        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(f"The joke:{joke}")
            speak(joke)

        elif 'exit' in query:
            print("Okay Bye. I am signing off...")
            speak('Okay Bye. I am signing off..')
            exit()
        else:
            break


        



    
