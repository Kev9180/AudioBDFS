from audio import *
from user_prompts import *
from termcolor import colored

def main():
    
    user_nums = get_nums()
    get_menu_choice()

    # for i in range(5):
    #     play_arpeggio(Chords.A_MAJOR.frequencies)
    # for i in range(5):
    #     play_arpeggio(Chords.A_MINOR.frequencies)

    # for i in range(10):
    #     play_note(Notes.C4.frequency)


    close_audio()

if __name__ == "__main__":
    main()