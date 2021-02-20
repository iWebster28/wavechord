import pyaudio
import numpy as np
import time

import chord as cd
import notes as nt

def play_note(root):
    # Piano sweep where i is the key #, A0 is key 0, C8 is key 88
    # for i in range(10, 88):
    p = pyaudio.PyAudio()
    fs = 44100
    volume = 0.5     # range [0.0, 1.0]
    
    # generate samples, note conversion to float32 array

    # FN for Scale Degrees
    # m7 = [1, b3, 5, b7]

    # Break into maj/min intervals [3, 4, 3]

    # FN for Scale Intervals
    m7_int = [0, 3, 7, 10]
    V7_int = [0, 4, 7, 10]
    M7_int = [0, 4, 7, 11]

    # FN to convert 49 -> A4 

    # To generate Chord Degrees - Am7:
    # Am7 = nt.gen_chord_degs(49, m7_int)
    # D7 = nt.gen_chord_degs(54, V7_int)

    chord_in = nt.gen_chord_degs(root, M7_int) # generate chord_in
    # Am7 = [nt.ntof(49), nt.ntof(52), nt.ntof(56), nt.ntof(59)]

    samples = cd.Chord(chord_in).samples

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples)
    stream.stop_stream()
    stream.close()
    p.terminate()