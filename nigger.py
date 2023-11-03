import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening... !")

    speak("I am jarvis Mam, please tell me how can i help you")


def takecommand():
    # it takes microphones input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()  # type: ignore

    # Logic for executing tasks based on query
    if "wikipedia" in query:
        speak("searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("http://www.youtube.com/watch")

    elif "open google" in query:
        webbrowser.open("google.com")
