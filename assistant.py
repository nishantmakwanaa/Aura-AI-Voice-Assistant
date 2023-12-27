import pyttsx3

import speech_recognition as sr 

import datetime

import wikipedia 

import webbrowser

import os

import smtplib

import requests

text_speech = pyttsx3.init()

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:

        speak("Good Morning Sir.")

    elif hour>=12 and hour<18:

        speak("Good Afternoon Sir.")   

    else:

        speak("Good Evening Sir.")  

    speak("Auraa This Side, Please Tell Me How May I Assist You ?")       

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        speak("Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print("Recognizing...")

        speak("Recognizing...")    

        query = r.recognize_google(audio, language='en-in')

        print(f"User Said : {query}\n")

    except Exception as e:

        print("Say That Again Please...")  

        return "None"
    
        return query

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.login('youremail@gmail.com', 'your-password')

    server.sendmail('youremail@gmail.com', to, content)

    server.close()

def news():

    main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=4276f3ac1f59444389c0f7778d86fcd8"

    news=requests.get(main_url).json()

    article=news["articles"]

    news_article=[]

    for arti in article:

        news_article.append(arti['title'])

    for i in range(10):

        print(i+1,news_article[i])

        text_speech.say(news_article[i])

        text_speech.runAndWait()

if __name__ == "__main__":

    wishMe()

    query = takeCommand()

    if query=='Hello Auraa':

        while True:
            
            if 'Hello Auraa'in query:

                query = query.replace("Hello Auraa", "")

            if 'wikipedia' in query:

                speak('Searching Wikipedia...')

                query = query.replace("wikipedia", "")

                results = wikipedia.summary(query, sentences=2)

                speak("According to Wikipedia")

                print(results)

                speak(results)

            elif 'Open YouTube' in query:

                webbrowser.open("youtube.com")

            elif 'Open Google' in query:

                webbrowser.open("google.com")

            elif 'Open Spotify' in query:

                webbrowser.open("https://open.spotify.com/")  

            elif 'time' in query:

                strTime = datetime.datetime.now().strftime("%H:%M:%S")

                print(f"Sir, The Time Is {strTime}")

                speak(f"Sir, The Time Is {strTime}")

            elif 'news' in query:

                news()

            elif 'Email To Harry' in query:

                try:

                    speak("What Should I Say?")

                    content = takeCommand()

                    to = "harryyourEmail@gmail.com"  
                    
                    sendEmail(to, content)

                    speak("Email Has Been Sent!")

                except Exception as e:

                    print(e)

                    speak("Sorry , I Am Not Able To Send This E-Mail")

            else:

                print("For Search Please Speak 'Hello Auraa' to search ")