import inspect
from sys import modules

import member_loader

'''Stores Function-formed algorithms for ease of self-creation'''
# TODO: find better word than 'creation', have no Dictionary for now.
# import Sorting_algorithms_pure as sa


def Status(data, blacklist=[]):
    'Used for Outputting variables with exceptions'

    output = []
    blacklist.append('END_indicator')

    for i in data.keys():
        for i2 in blacklist:
            if i2 == 'END_indicator':
                break

            if i2 in i:
                continue
            else:
                output.extend([i, str(data[i])])

    blacklist = []  # prevent storing previous items.
    print(' | '.join(output))


def Swap(a, b, c):
    a[b], a[c] = a[c], a[b]


def Bubble(array):
    swapped = True
    n = len(array)

    while swapped:
        swapped = False

        for idx in range(n - 1):

            if array[idx] > array[idx + 1]:
                swapped = True
                Swap(array, idx, idx + 1)
    return array


def Bubble_opt1(array):
    swapped = True
    n = len(array)

    while swapped:
        swapped = False

        for idx in range(n - 1):
            if array[idx] > array[idx + 1]:
                swapped = True
                Swap(array, idx, idx + 1)
        n -= 1

    return array

# In case more than one element is in final position, this is faster.


def Bubble_opt2(array):
    n = len(array)
    while True:
        newn = 0

        for idx in range(n - 1):
            if array[idx] > array[idx + 1]:
                Swap(array, idx, idx + 1)
                newn = idx + 1

        n = newn

        if n <= 1:
            break
    return array


def Cocktail_shaker(array):
    swapped = True
    flip = False
    start = 0
    end = len(array) - 1

    while swapped:
        swapped = False

        if flip:
            flip = False
            for idx in range(end, start, -1):
                if array[idx - 1] > array[idx]:
                    swapped = True
                    Swap(array, idx - 1, idx)
            start += 1

        else:
            flip = True
            for idx in range(start, end):
                if array[idx] > array[idx + 1]:
                    swapped = True
                    Swap(array, idx, idx + 1)
            end -= 1

    return array

    # idk why I spent 2 hours fixthing this. not sure why it's fixed.
    # needs further testing


def Cocktail_shaker_opt1(array):
    start = 0
    end = len(array) - 1
    import time

    while start <= end:
        # time.sleep(0.2)
        new_end = start
        new_start = end

        for idx in range(start, end):
            if array[idx] > array[idx + 1]:
                Swap(array, idx, idx + 1)
                new_end = idx

        end = new_end

        #Status(vars(), ['time'])

        for idx in range(end, start, -1):
            if array[idx - 1] > array[idx]:
                Swap(array, idx - 1, idx)
                new_start = idx - 1

        start = new_start

        #Status(vars(), ['time'])

    return array


def OddEven(array):
    swapped = True
    n = len(array)

    while swapped:
        swapped = False

        for idx in range(0, n - 1, 2):

            if array[idx] > array[idx + 1]:
                swapped = True
                Swap(array, idx, idx + 1)

        for idx in range(1, n - 1, 2):

            if array[idx] > array[idx + 1]:
                swapped = True
                Swap(array, idx, idx + 1)

    return array


def Selection(array):
    length = len(array)

    for loop in range(length):
        largest = 0

        for idx in range(length - loop):
            if array[idx] > array[largest]:
                largest = idx

        Swap(array, idx, largest)

    return array


def Insertion(array):
    length = len(array)

    for i in range(1, length):
        j = i

        while j > 0 and array[j - 1] > array[j]:
            Swap(array, j, j - 1)
            j -= 1

    return array


def Heap(array):

    def heapify(unsorted, idx, heap_size):
        # Understand this more, next time!
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

    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, i, n)

    for i in range(n - 1, 0, -1):
        Swap(array, 0, i)
        heapify(array, 0, i)

    return array


def Merge(array):
    L, R = 0, len(array) - 1

    def List_Merge(array, left, right, mid):
        Sorted = []
        l, r, m = left, right, mid + 1

        while(l <= mid and m <= right):

            if array[l] <= array[m]:
                Sorted.append(array[l])
                l += 1
            else:
                Sorted.append(array[m])
                m += 1

        if l > mid:
            for idx in range(m, right + 1):
                Sorted.append(array[idx])
        else:
            for idx in range(l, mid + 1):
                Sorted.append(array[idx])

        for idx in range(right, left - 1, -1):
            #Status(vars(), ['time'])
            array[idx] = Sorted.pop()

    def Sub_merge(array, left, right):

        if left < right:
            mid = (left + right) // 2
            Sub_merge(array, left, mid)
            Sub_merge(array, mid + 1, right)
            List_Merge(array, left, right, mid)

    Sub_merge(array, L, R)

    return array


def Quick(array):
    # TODO: understand this mother hubberd
    n = len(array)

    def Sub_Quick(left, right):

        if left < right:

            pivot_new = Partition(left, right)

            Sub_Quick(left, pivot_new)
            Sub_Quick(pivot_new + 1, right)

    def Partition(left, right):

        mid = (right + left) // 2

        if array[mid] < array[left]:
            Swap(array, mid, left)

        if array[right] < array[left]:
            Swap(array, right, left)

        pivot = array[mid]

        while True:
            while array[left] < pivot:
                left += 1

            while array[right] > pivot:
                right -= 1

            if left >= right:
                return right
            Swap(array, right, left)

    Sub_Quick(0, n - 1)
    return array


def Counting(array):
    n = len(array)
    m = max(array)

    counts = [0 for i in range(m + 1)]
    results = [0 for i in range(n)]

    for i in array:
        counts[i] += 1

    for i in range(m):
        counts[i + 1] += counts[i]

    for i in array:
        results[counts[i] - 1] = i
        counts[i] -= 1

    return results


def Radix_LSD_Base2(array):

    def count_bits(n):
        if(n == 0):
            return 0
        else:
            return 1 + count_bits(n >> 1)

    def counting_sort_bitwise(array, length, pos):

        counts = [0, 0]
        results = [0 for i in range(length)]

        for i in array:
            counts[i >> pos & 1] += 1

        counts[1] += counts[0]

        # Don't [::-1] waste Memory of another array size?
        for i in array[::-1]:

            results[counts[i >> pos & 1] - 1] = i
            counts[i >> pos & 1] -= 1

        # Tester(vars(), results)

        return results

    length = len(array)
    digit = count_bits(max(array))

    for i in range(digit):
        array = counting_sort_bitwise(array, length, i)

    return array


def Radix_LSD_BaseN(array, Base=10):
    
    def count_digits(n):
        if(n == 0):
            return 0
        else:
            return 1 + count_bits(n//Base)

    def counting_sort_bitwise(array, length, pos, Base=10):

        counts = [0, 0]
        results = [0 for i in range(length)]

        for i in array:
            counts[i//Base] += 1
            
        for idx in range(self.length):
            
            counts[idx + 1] += counts

        counts[1] += counts[0]

        # Don't [::-1] waste Memory of another array size?
        for i in array[::-1]:

            results[counts[i//Base] - 1] = i
            counts[i//Base] -= 1

        # Tester(vars(), results)

        return results

    length = len(array)
    digit = count_digits(max(array))

    for i in range(digit):
        array = counting_sort_bitwise(array, length, i)

    return array

# Can't fix darn noVNC to run on reverse proxy - for a week.
# p.s. To hyowon: Is this a bit too-lazy method for fillin' __all__?
excepts = ['Swap', 'Status']
__all__ = member_loader.ListFunction(
    __name__, name_only=True, blacklist=excepts)
