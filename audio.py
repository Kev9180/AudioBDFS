from enum import Enum
import numpy as np
import pyaudio

NOTE_LENGTH = 0.1   # duration in seconds
SAMPLE_RATE = 44100

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
    
class Chords(Enum):
    # Major chords
    C_MAJOR = [Notes.C4.frequency, Notes.E4.frequency, Notes.G4.frequency]
    D_MAJOR = [Notes.D4.frequency, Notes.F_SHARP4.frequency, Notes.A4.frequency]
    E_MAJOR = [Notes.E4.frequency, Notes.G_SHARP4.frequency, Notes.B4.frequency]
    F_MAJOR = [Notes.F4.frequency, Notes.A4.frequency, Notes.C5.frequency]
    G_MAJOR = [Notes.G4.frequency, Notes.B4.frequency, Notes.D5.frequency]
    A_MAJOR = [Notes.A4.frequency, Notes.C_SHARP5.frequency, Notes.E5.frequency]
    B_MAJOR = [Notes.B4.frequency, Notes.D_SHARP5.frequency, Notes.F_SHARP5.frequency]

    # Minor chords
    C_MINOR = [Notes.C4.frequency, Notes.D_SHARP4.frequency, Notes.G4.frequency]
    D_MINOR = [Notes.D4.frequency, Notes.F4.frequency, Notes.A4.frequency]
    E_MINOR = [Notes.E4.frequency, Notes.G4.frequency, Notes.B4.frequency]
    F_MINOR = [Notes.F4.frequency, Notes.G_SHARP4.frequency, Notes.C5.frequency]
    G_MINOR = [Notes.G4.frequency, Notes.A_SHARP4.frequency, Notes.D5.frequency]
    A_MINOR = [Notes.A4.frequency, Notes.C5.frequency, Notes.E5.frequency]
    B_MINOR = [Notes.B4.frequency, Notes.D5.frequency, Notes.F5.frequency]

    @property
    def frequencies(self):
        """Return the list of frequencies for this chord."""
        return self.value
    
# PyAudio globals
_pyaudio = None
_stream = None

def init_audio(SAMPLE_RATE):
    """Initialize PyAudio and a reusable stream"""
    global _pyaudio, _stream
    if _pyaudio is None:
        _pyaudio = pyaudio.PyAudio()
        _stream = _pyaudio.open(format=pyaudio.paFloat32,
                                channels=1,
                                rate=SAMPLE_RATE,
                                output=True)
        
def play_note(frequency, duration=NOTE_LENGTH, sample_rate=SAMPLE_RATE):
    """
    Play a sine wave at a specific frequency for a specific duration

    Args:
        frequency (float): Frequency of the note in Hz
        duration (float): Duration of note in seconds
        sample_rate (int): Sampling rate in Hz
    """

    init_audio(SAMPLE_RATE)
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = (np.sin(2 * np.pi * frequency * t) * 0.5).astype(np.float32)
    _stream.write(wave.tobytes())

def play_arpeggio(frequencies, duration=0.5, sample_rate=SAMPLE_RATE):
    """
    Plays multiple sine waves using a single PyAudio stream.

    Args:
        frequencies (list): List of frequencies in Hz to play.
        duration (float): Duration of each note in seconds.
        sample_rate (int): Sampling rate in Hz.
    """

    init_audio(SAMPLE_RATE)
    for frequency in frequencies:
        # Generate the sine wave for the current frequency
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = (np.sin(2 * np.pi * frequency * t) * 0.5).astype(np.float32)
        _stream.write(wave.tobytes())

def close_audio():
    """Close the PyAudio stream and terminate PyAudio."""
    global _pyaudio, _stream
    if _stream:
        _stream.stop_stream()
        _stream.close()
    if _pyaudio:
        _pyaudio.terminate()
    _stream = None
    _pyaudio = None    