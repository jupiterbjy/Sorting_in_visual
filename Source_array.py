import random
import member_loader


# Shuffling in Fisher-Yates way, with keyword arg.


def shuffle(array):

    def Swap(a, b, c):
        a[b], a[c] = a[c], a[b]

    length = len(array)

    for i in range(length):
        r = random.randint(0, length - i - 1)
        Swap(array, r, -1 - i)

    return array


def generate(length=20, zero_offset=1):

    return [i + zero_offset for i in range(length)]


def shuffle_generate(length, offset=1):
    return shuffle(generate(length, offset))


# Class storing testcase - shuffled array with delay.
# Signal is for syncing with output thread. Can't think better way
# for now. Python is pass-by-reference for sure so I'm giving a shot.


class Source():
    def __init__(self, length=-1, delay=0.5):
        self.length = length
        self.array = shuffle(generate(length))
        self.delay = delay


__all__ = member_loader.ListFunction(__name__)
