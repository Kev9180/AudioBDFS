from audio import *

def main():
    arpeggio = [Notes.C4.frequency, Notes.E4.frequency, Notes.G4.frequency]

    for i in range(6):
        play_frequency(arpeggio, duration=0.15)

    close_stream()

if __name__ == "__main__":
    main()