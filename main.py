from audio import *
from user_prompts import *
from termcolor import colored

def main():
    get_menu_choice()

    for i in range(5):
        play_note(Notes.C6.frequency)


    close_audio()

if __name__ == "__main__":
    main()