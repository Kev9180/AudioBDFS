from audio import *

def main():

    for i in range(3):
        play_arpeggio(Chords.C_MAJOR.frequencies, duration=0.15)
    
    for i in range(3):
        play_arpeggio(Chords.F_MAJOR.frequencies, duration=0.15)

    play_arpeggio(Chords.G_MAJOR.frequencies, duration=0.15)
    play_arpeggio(Chords.F_MAJOR.frequencies, duration=0.15)
    play_arpeggio(Chords.E_MINOR.frequencies, duration=0.15)
    play_arpeggio(Chords.C_MAJOR.frequencies, duration=0.15)


    close_audio()

if __name__ == "__main__":
    main()