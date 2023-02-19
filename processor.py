import pyttsx3
import datetime
import speech_recognition as sr
import wolframalpha
import config

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client(config.api_key)

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def say(audio):
    print('Info-chan: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greet_me():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        say('Good Morning Kevin, It\'s your assistant Info-chan!')

    elif 12 <= current_hour < 18:
        say('Good Afternoon Kevin, It\'s your assistant Info-chan!')

    elif current_hour >= 18 and current_hour != 0:
        say('Good Evening Kevin, It\'s your assistant Info-chan!')


def give_command():
    k = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        k.pause_threshold = 1
        audio = k.listen(source)
    try:
        command = k.recognize_google(audio, language='en-us')
        print('Kevin Jonathan: ' + command + '\n')

    except sr.UnknownValueError:
        say('Sorry! I didn\'t quite catch that! Try typing it here!')
        command = str(input('Command: '))

    except:
        say('Sorry! I can\'t process the command for now, please try typing it here!')
        command = str(input('Command: '))

    return command
