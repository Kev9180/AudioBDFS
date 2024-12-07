from enum import Enum

# Using frequencies for now - will update depending on which sound lib is used
class Notes(Enum):
    C = 261.63
    C_SHARP = 277.18
    D = 293.66
    D_SHARP = 311.13
    E = 329.63
    F = 349.23
    F_SHARP = 369.99
    G = 392.00
    G_SHARP = 415.30
    A = 440.00
    A_SHARP = 466.16
    B = 493.88

    @property
    def frequency(self):
        return self.value
