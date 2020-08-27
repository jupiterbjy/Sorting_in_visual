import array


def Swap(arr: array.array, idx1: int, idx2: int):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


def bubble(arr: array.array):
    swapped = True
    n = len(arr)

    while swapped:
        swapped = False

        for idx in range(n - 1):
            if arr[idx] > arr[idx + 1]:
                swapped = True
                Swap(arr, idx, idx + 1)
    return arr
