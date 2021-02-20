import numpy as np


# Ian Webster
# 2/20/21
# A Chord generator using numpy. Works with pyaudio

class Chord():
    def __init__(self, freqs=[440], fs=44100, duration=1.5):
        self.n = len(freqs) # Num notes in chord
        self.samples = sum([np.sin(2*np.pi*np.arange(fs*duration)*f/fs).astype(np.float32)/self.n for f in freqs])
    


