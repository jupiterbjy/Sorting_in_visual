from typing import MutableSequence


def Bubble(arr: MutableSequence):
    swapped = True
    n = len(arr)

    while swapped:
        swapped = False

        for idx in range(n - 1):
            if arr[idx] > arr[idx + 1]:
                swapped = True
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        n -= 1
    # return arr


def Bubble_opt1(arr: MutableSequence):
    n = len(arr)
    while True:
        new_n = 0

        for idx in range(n - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                new_n = idx + 1

        n = new_n

        if n <= 1:
            break
    # return arr


def Cocktail_shaker(arr: MutableSequence):
    swapped = True
    flip = False
    start = 0
    end = len(arr) - 1

    while swapped:
        swapped = False

        if flip:
            flip = False
            for idx in range(end, start, -1):
                if arr[idx - 1] > arr[idx]:
                    swapped = True
                    arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            start += 1

        else:
            flip = True
            for idx in range(start, end):
                if arr[idx] > arr[idx + 1]:
                    swapped = True
                    arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
            end -= 1

    # return arr


def Cocktail_shaker_opt1(arr: MutableSequence):
    start = 0
    end = len(arr) - 1

    while start <= end:
        new_end = start
        new_start = end

        for idx in range(start, end):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                new_end = idx

        end = new_end

        for idx in range(end, start, -1):
            if arr[idx - 1] > arr[idx]:
                arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
                new_start = idx - 1

        start = new_start

    # return arr


def OddEven(arr: MutableSequence):
    swapped = True
    n = len(arr)

    while swapped:
        swapped = False

        for idx in range(0, n - 1, 2):

            if arr[idx] > arr[idx + 1]:
                swapped = True
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

        for idx in range(1, n - 1, 2):

            if arr[idx] > arr[idx + 1]:
                swapped = True
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    # return arr
