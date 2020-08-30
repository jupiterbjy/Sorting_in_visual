from collections.abc import MutableSequence


def bubble(arr: MutableSequence):
    swapped = True
    n = len(arr)

    while swapped:
        swapped = False

        for idx in range(n - 1):
            if arr[idx] > arr[idx + 1]:
                swapped = True
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    return arr


if __name__ == '__main__':
    from random import shuffle
    from new_support import ArrayWrap
    arr = ArrayWrap(list(i for i in range(20)))
    shuffle(arr)
    print(arr)
    print(bubble(arr))
