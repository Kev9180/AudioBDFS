from audio import *
import numpy as np
import time

def main():

    # play_arpeggio(Chords.B_MINOR.frequencies)
    # play_arpeggio(Chords.A_MINOR.frequencies)
    # play_arpeggio(Chords.G_MINOR.frequencies)

    for i in np.linspace(0, 5, 10):
        play_note(Notes.C4.frequency, effect="distortion", level=i)


    for i in range(10):
        play_note(Notes.C4.frequency)


    close_audio()

if __name__ == "__main__":
    main()