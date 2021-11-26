from typing import MutableSequence


def Selection(arr: MutableSequence):
    length = len(arr)

    for loop in range(length):
        largest = 0

        for idx in range(length - loop):
            if arr[idx] > arr[largest]:
                largest = idx

        # noinspection PyUnboundLocalVariable
        arr[idx], arr[largest] = arr[largest], arr[idx]

    # return arr


def Heap(arr: MutableSequence):
    def heapify(unsorted, idx, heap_size):
        largest = idx
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2

        if left_idx < heap_size and unsorted[left_idx] > unsorted[largest]:
            largest = left_idx

        if right_idx < heap_size and unsorted[right_idx] > unsorted[largest]:
            largest = right_idx

        if largest != idx:
            unsorted[largest], unsorted[idx] = unsorted[idx], unsorted[largest]
            heapify(unsorted, largest, heap_size)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    # return arr
