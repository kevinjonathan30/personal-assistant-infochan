import os
import random
import sys
import webbrowser
import wikipedia
import processor
import requests
from googlesearch import search


def process_intent(command):
    if 'open' in command:
        command = command.replace('open', '')
        search_result_list = list(search(command))
        page = requests.get(search_result_list[0])
        webbrowser.open(page.url)

    elif "what\'s up" in command or 'how are you' in command:
        set_replies = ['I\'m doing okay', 'I\'m doing great, thanks for asking!', 'Not too bad',
                       'Could be better, but I\'m hanging in there.']
        processor.say(random.choice(set_replies))

    elif "who are you" in command or 'what are you' in command:
        set_replies = [' I am Info-chan', 'I am an AI created by Kevin Jonathan']
        processor.say(random.choice(set_replies))

    elif 'nothing' in command or 'abort' in command or 'stop' in command:
        processor.say('Okay bye, have a good day.')
        sys.exit()

    elif 'hello' in command or 'hi' in command:
        processor.say('Heyho!')

    elif 'bye' in command:
        processor.say('Bye, have a great day.')
        sys.exit()

    elif 'play music' in command:
        music_folder = 'C:\\Users\\Public\\Music\\'
        processor.say('Okay, what\'s the music title?')
        music_title = processor.give_command()
        music = music_folder + music_title + '.mp3'
        os.system(music)

        processor.say('Okay, here is your music! Enjoy!')

    elif 'show images' in command:
        images_folder = 'C:\\Users\\Public\\Pictures\\'
        processor.say('Okay, what\'s the image name?')
        image_title = processor.give_command()
        image = images_folder + image_title + '.jpeg'
        os.system(image)

        processor.say('Okay, here is your image!')

    else:
        processor.say('Sure, searching...')
        try:
            try:
                res = processor.client.Input(command)
                outputs = next(res.outputs).text
                processor.say('If I remember correctly..')
                processor.say(outputs)

            except:
                outputs = wikipedia.summary(command, sentences=3)
                processor.say('According to Wikipedia..')
                processor.say(outputs)

        except:
            processor.say("Searching on google for " + command)
            command = command.replace(' ', '+')
            webbrowser.open('https://www.google.com/search?q=' + command)
