from math import floor

def fmod(x, b):
    return x - b * floor(x / b)