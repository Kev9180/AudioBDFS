from enum import Enum
import numpy as np
import pyaudio

NOTE_LENGTH = 0.1   # duration in seconds

class Notes(Enum):
    # Octave 3
    C3 = 130.81
    C_SHARP3 = 138.59
    D3 = 146.83
    D_SHARP3 = 155.56
    E3 = 164.81
    F3 = 174.61
    F_SHARP3 = 185.00
    G3 = 196.00
    G_SHARP3 = 207.65
    A3 = 220.00
    A_SHARP3 = 233.08
    B3 = 246.94

    # Octave 4
    C4 = 261.63
    C_SHARP4 = 277.18
    D4 = 293.66
    D_SHARP4 = 311.13
    E4 = 329.63
    F4 = 349.23
    F_SHARP4 = 369.99
    G4 = 392.00
    G_SHARP4 = 415.30
    A4 = 440.00
    A_SHARP4 = 466.16
    B4 = 493.88

    # Octave 5
    C5 = 523.25
    C_SHARP5 = 554.37
    D5 = 587.33
    D_SHARP5 = 622.25
    E5 = 659.25
    F5 = 698.46
    F_SHARP5 = 739.99
    G5 = 783.99
    G_SHARP5 = 830.61
    A5 = 880.00
    A_SHARP5 = 932.33
    B5 = 987.77

    # Octave 6
    C6 = 1046.50
    C_SHARP6 = 1108.73
    D6 = 1174.66
    D_SHARP6 = 1244.51
    E6 = 1318.51
    F6 = 1396.91
    F_SHARP6 = 1479.98
    G6 = 1567.98
    G_SHARP6 = 1661.22
    A6 = 1760.00
    A_SHARP6 = 1864.66
    B6 = 1975.53

    @property
    def frequency(self):
        return self.value
    
# Define and instantiate a PyAudio object to work with
p = pyaudio.PyAudio()
stream = None

def play_frequency(frequencies, duration=0.5, sample_rate=44100):
    """
    Plays multiple sine waves seamlessly using a single PyAudio stream.

    Args:
        frequencies (list): List of frequencies in Hz to play.
        duration (float): Duration of each note in seconds.
        sample_rate (int): Sampling rate in Hz.
    """
    global stream

    if stream is None:
        # Initialize the PyAudio stream (only once for seamless playback)
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=sample_rate,
                        output=True)

    for frequency in frequencies:
        # Generate the sine wave for the current frequency
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = (np.sin(2 * np.pi * frequency * t) * 0.5).astype(np.float32)
        
        # Write the waveform to the stream (seamless playback)
        stream.write(wave.tobytes())

def close_stream():
    """Close the global PyAudio stream."""
    global stream
    if stream is not None:
        stream.stop_stream()
        stream.close()
    p.terminate()
    