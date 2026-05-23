import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import os
import pyjokes

# Initialize speech engine
engine = pyttsx3.init()

# Initialize recognizer
recognizer = sr.Recognizer()


def speak(text):
    print("Manali:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)

        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError as e:
        print("Error:", e)
        return ""


def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def tell_date():
    current_date = datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {current_date}")


def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)


if __name__ == "__main__":

    speak("Hi Nakrani, I am Manali. How may I help you?")

    while True:

        command = listen()

        if not command:
            continue

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "hello" in command:
            speak("Hello Meet. Nice to talk with you.")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open instagram" in command:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        elif "open facebook" in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

        elif "open safari" in command:
            speak("Opening Safari")
            os.system("open -a Safari")

        elif "open chrome" in command:
            speak("Opening Chrome")
            os.system("open -a 'Google Chrome'")

        elif "tell me a joke" in command or "joke" in command:
            tell_joke()

        elif "exit" in command or "stop" in command:
            speak("Goodbye Meet")
            break

        else:
            speak(f"You said {command}")