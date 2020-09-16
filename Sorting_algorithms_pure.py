import GetModuleReference
import array
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


def Insertion(arr: MutableSequence):
    for i in range(1, len(arr)):
        j = i

        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

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


def Merge(arr: MutableSequence):

    def join_parts(array_, left, right, mid):
        sorted_ = array.array('i')
        l_, r, m = left, right, mid + 1

        while l_ <= mid and m <= right:

            if array_[l_] <= array_[m]:
                sorted_.append(array_[l_])
                l_ += 1
            else:
                sorted_.append(array_[m])
                m += 1

        if l_ > mid:
            for idx in range(m, right + 1):
                sorted_.append(array_[idx])
        else:
            for idx in range(l_, mid + 1):
                sorted_.append(array_[idx])

        for idx in range(right, left - 1, -1):
            array_[idx] = sorted_.pop()

    def sub_merge(array_, left, right):

        if left < right:
            mid = (left + right) // 2
            sub_merge(array_, left, mid)
            sub_merge(array_, mid + 1, right)
            join_parts(array_, left, right, mid)

    sub_merge(arr, 0, len(arr) - 1)

    # return arr


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

    counts = array.array('i', (0 for _ in range(m + 1)))
    results = array.array('i', (0 for _ in range(n)))

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

    def counting_sort_bitwise(array_, length_, pos):

        counts = array.array('i', (0, 0))
        results = array.array('i', (0 for _ in range(length_)))

        for i_ in array_:
            counts[i_ >> pos & 1] += 1

        counts[1] += counts[0]

        for i_ in reversed(array_):
            results[counts[i_ >> pos & 1] - 1] = i_
            counts[i_ >> pos & 1] -= 1

        return results

    length = len(arr)
    digit = count_bits(max(arr))

    for i in range(digit):
        # arr = counting_sort_bitwise(arr, length, i)
        # going one more loop to 'update' arr, not 'aliasing' to new object.
        for idx, val in enumerate(counting_sort_bitwise(arr, length, i)):
            arr[idx] = val

    # return arr


def _Radix_LSD_BaseN(arr: MutableSequence, base):

    def count_digits(n):
        if n == 0:
            return 0
        else:
            return 1 + count_digits(n // base)

    def counting_sort_custom(array_, length_, pos):

        def Base_out(n):
            return (n // base ** pos) % base

        counts = array.array('i', (0 for _ in range(base)))
        results = array.array('i', (0 for _ in range(length_)))

        for i_ in array_:
            counts[Base_out(i_)] += 1

        for i_ in range(base - 1):
            counts[i_ + 1] += counts[i_]

        for i_ in reversed(array_):

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
    return _Radix_LSD_BaseN(arr, 10)


def Radix_LSD_Base4(arr):
    return _Radix_LSD_BaseN(arr, 4)

# TODO: Make bit_shift version of LSDs' whose base is multiply of 2.
# TODO: separate sorts into respective .py files for easier access to reused components.


def WikiSort_in_place(arr: MutableSequence, _64bit=False):
    """Implementation based on:
    https://github.com/BonzaiThePenguin/WikiSort/blob/master/Chapter%201.%20Tools.md"""

    def swap(arr_, idx1, idx2):
        arr_[idx1], arr_[idx2] = arr_[idx2], arr_[idx1]

    def reverse(arr_, range_: range):
        for idx in range(len(range_) // 2 - 1, -1, -1):
            swap(arr_, range_.start + idx, range_.stop - idx - 1)

    def rotate(arr_, range_: range, amount):
        reverse(arr_, range(range_.start, range_.start + amount))
        reverse(arr_, range(range_.start + amount, range_.stop))
        reverse(arr_, range_)

    def _binary_main(arr_, range_: range, val, comp):
        start_ = range_.start
        end_ = range_.stop
        while start_ < end_:
            mid_ = start_ + (end_ - start_) // 2
            if comp(arr_[mid_], val):
                start_ = mid_ + 1
            else:
                end_ = mid_

        if start_ == range_.stop and comp(arr_[start_], val):
            start_ = start_ + 1
        return start_

    def binary_first(arr_, range_: range, val):
        return _binary_main(arr_, range_, val, lambda x, y: x < y)

    def binary_last(arr_, range_: range, val):
        return _binary_main(arr_, range_, val, lambda x, y: x <= y)

    def length_gen(start_, stop_, multiply_factor=1):
        """Step is self value."""
        curr = start_
        while curr < stop_:
            yield curr
            curr *= multiply_factor

    def insertion(arr_: MutableSequence, start_, end_):
        for i in range(start_, end_):
            j = i

            while j > start_ and arr_[j - 1] > arr_[j]:
                swap(arr_, j, j - 1)
                j -= 1

    def merge_in_place(arr_, range_a, range_b):
        while len(range_a) > 0 and len(range_b) > 0:
            mid_ = binary_first(arr_, range_b, arr_[range_a.start])
            amount = mid_ - range_a.stop
            rotate(arr_, range(range_a.start, mid_), amount)

            range_b = range(mid_, range_b.stop)
            range_a = range(range_a.start + amount, mid_)
            range_a = range(binary_last(arr_, range_a, arr_[range_a.start]), mid_)

    def floor_by_power_2(x: int):
        for n in range(6 if _64bit else 5):
            x = x | (x >> 2**n)
        else:
            return x - (x >> 1)

    # main loop

    power_of_two = floor_by_power_2(len(arr))
    scale = len(arr) / power_of_two

    for merge in range(0, power_of_two, 16):
        start = int(merge * scale)
        end = int(start + 16 * scale)
        insertion(arr, start, end)

    for length in length_gen(16, power_of_two, multiply_factor=2):
        for merge in range(0, power_of_two, 2 * length):

            start = int(merge * scale)
            mid = int((merge + length) * scale)
            end = int((merge + length * 2) * scale)

            if arr[end - 1] < arr[start]:
                rotate(arr, range(start, end), mid - start)
            elif arr[mid - 1] > arr[mid]:
                merge_in_place(arr, range(start, mid), range(mid, end))


__all__ = GetModuleReference.ListFunction(__name__)

if __name__ == '__main__':
    testcase = [i for i in range(100)]
    from async_main import shuffle
    shuffle(testcase)
    print(testcase)
    WikiSort_in_place(testcase)
    print(testcase)
