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


def Heap2(arr: MutableSequence):
    def heapify(arr_, root, heap_size):
        e = arr_[root]

        largest = 2 * root
        while largest <= heap_size:

            if largest < heap_size and arr_[largest] < arr_[largest + 1]:
                largest += 1

            if e >= arr_[largest]:
                break

            arr_[largest // 2] = arr_[largest]

            largest *= 2

        arr_[largest // 2] = e

    n = len(arr)

    for i in range(n // 2, 0, -1):
        heapify(arr, i - 1, n - 1)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i - 1)


def Heap(arr: MutableSequence):
    def heapify(unsorted, root, heap_size):
        largest = root
        left_idx = 2 * root + 1
        right_idx = 2 * root + 2

        if left_idx < heap_size and unsorted[left_idx] > unsorted[largest]:
            largest = left_idx

        if right_idx < heap_size and unsorted[right_idx] > unsorted[largest]:
            largest = right_idx

        if largest != root:
            unsorted[largest], unsorted[root] = unsorted[root], unsorted[largest]
            heapify(unsorted, largest, heap_size)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    # return arr
