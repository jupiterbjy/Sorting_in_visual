import random


# Shuffling in Fisher-Yates way, with keyword arg.

def shuffle(array, length = -1):
    if length < 0:
        length = len(array)
    
    for i in range(length):
        r = random.randint(0, length-i)
        array[r], array[-1-i] = array[-1-i], array[r]
    
    return array


# Class storing testcase - shuffled array with delay.
# Signal is for syncing with output thread. Can't think better way
# for now. Python is pass-by-reference for sure so I'm giving a shot.

class Source():
    def __init__(self, length = -1, delay = 50):
        self.length = length
        self.array = shuffle([i for i in range(length)], length)
        self.signal = False
        self.sorted = False
