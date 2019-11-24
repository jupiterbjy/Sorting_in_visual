import random


# Shuffling in Fisher-Yates way, with keyword arg.
def Swap(a, b, c):
    a[b], a[c] = a[c], a[b]


def shuffle(array, length=-1):
    if length < 0:
        length = len(array)

    for i in range(length):
        r = random.randint(0, length - i - 1)
        Swap(array, r, -1 - i)

    return array


# Class storing testcase - shuffled array with delay.
# Signal is for syncing with output thread. Can't think better way
# for now. Python is pass-by-reference for sure so I'm giving a shot.


class Source():
    def __init__(self, length=-1, delay=0.5):
        self.length = length
        self.array = shuffle([i + 1 for i in range(length)], length)
        self.delay = delay
