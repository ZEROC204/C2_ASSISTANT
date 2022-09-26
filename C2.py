import keyboard
import selenium
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress

from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good EveninG!")

    assname = ("C2")
    speak("my name is C2........")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Zero: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'spotify' in query:
            speak('Searching spotify..')
            query = query.replace("spotify","")
            webbrowser.open(f"https://open.spotify.com/search/{query}")

        elif 'whatsapp' in query:
            speak('opening whatsapp...')
            webbrowser.open("https://web.whatsapp.com/")

        elif 'wordpress' in query:
            speak('opening wordpress..')
            webbrowser.open('https://wordpress.com')

        elif 'google meet' in query:
            speak('enter meeting code')
            code = input("Enter meeting code: ")
            speak('opening google meet..')
            webbrowser.open(f"https://meet.google.com/{code}")
            time.sleep(3)
            keyboard.press_and_release('ctrl+e, space')
            time.sleep(1)
            keyboard.press_and_release('ctrl+d, space')
            time.sleep(1)
            speak('click ask to join..')
            speak('thank you')

        elif 'telegram' in query:
            speak('opening telegram')
            webbrowser.open("https://webk.telegram.org/")

        elif 'wikihow' in query:
            speak('opening wikihow..')
            query = query.replace("wikihow","")
            webbrowser.open(f"https://www.wikihow.com/wikiHowTo?search={query}")

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'hello' in query:
            speak('hi there..')



        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'open my blog' in query:
            speak('okay')
            webbrowser.open('thegeekdbinary.wordpress.com')

        elif 'view my blog' in query:
            speak('okay')
            webbrowser.open('thegeekdbinary.wordpress.com')

        elif 'calendar' in query:
            speak('okay')
            from calendar import *
            yr = input("Enter year: ")
            print(month(int(yr), 1))
            print(month(int(yr), 2))
            print(month(int(yr), 3))
            print(month(int(yr), 4))
            print(month(int(yr), 5))
            print(month(int(yr), 6))
            print(month(int(yr), 7))
            print(month(int(yr), 8))
            print(month(int(yr), 9))
            print(month(int(yr), 10))
            print(month(int(yr), 11))
            print(month(int(yr), 12))


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'why are you here' in query:
            speak('because you made a promise about our future together')

        elif 'why are you like this' in query:
            speak('Do you know why snow is white..')
            speak('because its forgotten what colour its supposed to be...')

        elif 'look at my zero mask' in query:
            speak('that mask is heavier than it looks')
            speak('the bearer wears a fate not just of the anime community but that of the world ')

        elif 'geass' in query:
            speak('i said that geass was the power of the king which would condemn you to a life of solitude  ')
            speak('maybe thats not quite correct right')

        elif 'you are a monster' in query:
            speak("don't you hate me for cheating you out of your own life ")
            speak('by giving you your geass i affected your life and drastically changed your fate')

        elif 'who are you' in query:
            speak('all i have left are my memories from when i was a witch')
            speak('other than that i don')

        elif 'helping me' in query:
            speak('its because we have a contract')

        elif 'help me' in query:
            speak('we have our contract..')
            speak('i will stay with you to the very end..')

        elif 'thank you' in query:
            speak('well then')
            speak('Can you show your appreciation..')
            speak('say my name like you did it before')
            speak('just this once with tenderness like you treasure it in your heart')

        elif 'i did it' in query:
            print('C2:Did you use your geass..?')
            speak('did you use your geass')

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'how old are you' in query:
            speak('i am an immortal and i am not used to counting')

        elif 'you are annoying' in query:
            speak('why are you so ')


        elif 'bye' in query:
            speak('bye..')
            exit()

        elif 'answer my question' in query:
            speak("did you forget that your geass wouldn't work on me..")

        elif 'you are bad' in query:
            speak('but you used to tell me that i am an immortal witch')

        elif 'can you get smarter' in query:
            speak('i am already smart')

        elif 'you are beautiful' in query:
            speak("so you don't hate the snow..")

        elif 'what is your birth date' in query:
            speak("i can't remember")

        elif 'you are boring' in query:
            speak('i have been living for decades and decades..')
            speak('and you are the only one i found similar to me...')

        elif 'who is your boss' in query:
            speak('i am')

        elif 'are you busy' in query:
            speak('a little')
            speak("i am checking the internet about the world's largest pizza")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('C2.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)



        elif "show note" in query:
            speak("Showing Notes")
            file = open("C2.txt", "r")
            print(file.read())
            speak(file.read(6))


        elif "weather" in query:
            api_key = "b211515c97f8d4869e5eb437540ecaf2"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))


        elif "calculate" in query:

            app_id = "4W5VQ4-YUV8Q2KW7A"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)
            time.sleep(5)


        elif 'what' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takeCommand()
            app_id = "4W5VQ4-YUV8Q2KW7A "
            client = wolframalpha.Client('4W5VQ4-YUV8Q2KW7A')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
