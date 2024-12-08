from notes import *

def main():
    arpeggio = [Notes.C4.frequency, Notes.E4.frequency, Notes.G4.frequency]

    play_sine_wave_seamless(arpeggio, duration=0.15)

    close_stream()

if __name__ == "__main__":
    main()