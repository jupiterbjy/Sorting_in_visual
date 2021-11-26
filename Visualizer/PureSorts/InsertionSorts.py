from typing import MutableSequence


def Insertion(arr: MutableSequence):
    for i in range(1, len(arr)):
        j = i
        item = arr[i]

        while j > 0 and arr[j - 1] > item:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = item

