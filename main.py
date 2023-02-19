import processor
import intent

if __name__ == '__main__':
    processor.greet_me()
    processor.say('what is your first command?')

    while True:
        command = processor.give_command()
        command = command.lower()

        intent.process_intent(command)

        processor.say('What is your next command?')
