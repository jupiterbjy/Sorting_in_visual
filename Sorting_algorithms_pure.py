from Tools import member_loader
from collections.abc import MutableSequence


def Bubble(arr: MutableSequence):
    swapped = True
    n = len(arr)

    while swapped:
        swapped = False

        for idx in range(n - 1):
            if arr[idx] > arr[idx + 1]:
                swapped = True
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    return arr


def Bubble_opt1(arr: MutableSequence):
    swapped = True
    n = len(arr)

    while swapped:
        swapped = False

        for idx in range(n - 1):
            if arr[idx] > arr[idx + 1]:
                swapped = True
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        n -= 1

    return arr

# In case more than one element is in final position, this is faster.


def Bubble_opt2(arr: MutableSequence):
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
    return arr


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

    return arr


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

    return arr


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

    return arr


def Selection(arr: MutableSequence):
    length = len(arr)

    for loop in range(length):
        largest = 0

        for idx in range(length - loop):
            if arr[idx] > arr[largest]:
                largest = idx

        arr[idx], arr[largest] = arr[largest], arr[idx]

    return arr


def Insertion(arr: MutableSequence):
    length = len(arr)

    for i in range(1, length):
        j = i

        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


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

    return arr


def Merge(arr: MutableSequence):

    def join_parts(array, left, right, mid):
        sorted_ = []
        l_, r, m = left, right, mid + 1

        while l_ <= mid and m <= right:

            if array[l_] <= array[m]:
                sorted_.append(array[l_])
                l_ += 1
            else:
                sorted_.append(array[m])
                m += 1

        if l_ > mid:
            for idx in range(m, right + 1):
                sorted_.append(array[idx])
        else:
            for idx in range(l_, mid + 1):
                sorted_.append(array[idx])

        for idx in range(right, left - 1, -1):
            array[idx] = sorted_.pop()

    def sub_merge(array, left, right):

        if left < right:
            mid = (left + right) // 2
            sub_merge(array, left, mid)
            sub_merge(array, mid + 1, right)
            join_parts(array, left, right, mid)

    sub_merge(arr, 0, len(arr) - 1)

    return arr


def Quick(arr: MutableSequence):
    n = len(arr)

    def Sub_Quick(left, right):

        if left < right:

            pivot_new = Partition(left, right)

            Sub_Quick(left, pivot_new)
            Sub_Quick(pivot_new + 1, right)

    def Partition(left, right):

        mid = (right + left) // 2

        if arr[mid] < arr[left]:
            arr[mid], arr[left] = arr[left], arr[mid]

        if arr[right] < arr[left]:
            arr[right], arr[left] = arr[left], arr[right]

        pivot = arr[mid]

        while True:
            while arr[left] < pivot:
                left += 1

            while arr[right] > pivot:
                right -= 1

            if left >= right:
                return right

            arr[right], arr[left] = arr[left], arr[right]

    Sub_Quick(0, n - 1)
    # return arr


def Counting(arr: MutableSequence):
    n = len(arr)
    m = max(arr)

    counts = [0 for _ in range(m + 1)]
    results = [0 for _ in range(n)]

    for i in arr:
        counts[i] += 1

    for i in range(m):
        counts[i + 1] += counts[i]

    for i in arr:
        results[counts[i] - 1] = i
        counts[i] -= 1

    # return results

    for idx, val in enumerate(results):
        arr[idx] = val

    # return arr


def Radix_LSD_Base2(arr: MutableSequence):

    def count_bits(n):
        if n == 0:
            return 0
        else:
            return 1 + count_bits(n >> 1)

    def counting_sort_bitwise(array, length_, pos):

        counts = [0, 0]
        results = [0 for _ in range(length_)]

        for i_ in array:
            counts[i_ >> pos & 1] += 1

        counts[1] += counts[0]

        for i_ in reversed(array):
            results[counts[i_ >> pos & 1] - 1] = i_
            counts[i_ >> pos & 1] -= 1

        return results

    length = len(arr)
    digit = count_bits(max(arr))

    for i in range(digit):
        # arr = counting_sort_bitwise(arr, length, i)
        # going one more loop to 'update' arr, not 'aliasing' to new object.
        for idx, val in counting_sort_bitwise(arr, length, i):
            arr[idx] = val

    # return arr


def Radix_LSD_BaseN(arr: MutableSequence, base):

    def count_digits(n):
        if n == 0:
            return 0
        else:
            return 1 + count_digits(n // base)

    def counting_sort_custom(array, length_, pos):

        def Base_out(n):
            return (n // base ** pos) % base

        counts = [0 for _ in range(base)]
        results = [0 for _ in range(length_)]

        for i_ in array:
            counts[Base_out(i_)] += 1

        for idx in range(base - 1):
            counts[idx + 1] += counts[idx]

        for i_ in reversed(array):

            results[counts[Base_out(i_)] - 1] = i_
            counts[Base_out(i_)] -= 1

        return results

    length = len(arr)
    digit = count_digits(max(arr))

    for i in range(digit):
        # arr = counting_sort_custom(arr, length, i)
        # going one more loop to 'update' arr, not 'aliasing' to new object.
        for idx, val in enumerate(counting_sort_custom(arr, length, i)):
            arr[idx] = val

    # return arr


def Radix_LSD_Base10(arr):
    return Radix_LSD_BaseN(arr, 10)


def Radix_LSD_Base4(arr):
    return Radix_LSD_BaseN(arr, 4)

# TODO: Make bit_shift version of LSDs' whose base is multiply of 2.


excepts = ['Radix_LSD_BaseN']
__all__ = member_loader.ListFunction(__name__, blacklist=excepts)
