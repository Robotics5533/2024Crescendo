from math import floor

def fmod(x, b):
    return x - b * floor(x / b)

def clamp(x, mi, ma):
    return max(mi, min(x,ma))
    