# Ian Webster
# 2/20/21
# Functions to calculate note frequencies based on piano key

def ntof(i):
    """
    Convert piano key `i` to frequency `f`
    f(n) = 2^((n - 49) / 12) * 440 Hz (for n in range 1-88 keyth of piano)
    https://en.wikipedia.org/wiki/Piano_key_frequencies
    """
    f = 2 ** ((i - 49) / 12) * 440
    return f

def gen_chord_degs(root, degs):
    """
    Given root note number `i` and scale degrees, generates chord degrees in frequency format [Hz]
    """
    chord_degs = [ntof(root + intvl) for intvl in degs]
    print(chord_degs)
    return chord_degs