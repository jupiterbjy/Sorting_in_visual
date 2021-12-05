import GetModuleReference
import array
from collections.abc import MutableSequence


def Quick(arr: MutableSequence):

    def inner(arr_, left, right):

        if left < right:
            i = left
            j = right + 1
            pivot = arr_[left]

            while True:
                while True:
                    i += 1
                    if not arr_[i] < pivot:
                        break

                while True:
                    j -= 1
                    if not arr_[j] > pivot:
                        break

                if i < j:
                    arr_[i], arr_[j] = arr_[j], arr_[i]

                if not i < j:
                    break

            arr_[left], arr_[j] = arr_[j], arr_[left]

            inner(arr_, left, j - 1)
            inner(arr_, j + 1, right)

    inner(arr, 0, len(arr) - 1)


def _Quick(arr: MutableSequence):
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


def shell(arr: MutableSequence):
    # ratsgo.github.io

    def gap_insertion(arr_, first, gap):
        for i in range(first + gap, len(arr_), gap):
            cur_val = arr_[i]
            pos = i

            while pos >= gap and arr_[pos - gap] > cur_val:
                arr_[pos] = arr_[pos - gap]
                pos -= gap

            arr_[pos] = cur_val

    def shell_main(arr_):
        sublist_count = len(arr_) // 2

        while sublist_count > 0:
            if sublist_count & 1 == 0:
                sublist_count += 1

            for start_pos in range(sublist_count):
                gap_insertion(arr_, start_pos, sublist_count)

            sublist_count //= 2

    shell_main(arr)


def cycle(arr: MutableSequence):
    # wikipedia implementation

    for cycle_start in range(0, len(arr) - 1):
        item = arr[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == arr[pos]:
            pos += 1

        arr[pos], item = item, arr[pos]

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]


def bucket(arr):
    from itertools import chain

    k = len(arr)

    def insertion(arr_: MutableSequence):
        for idx_ in range(len(arr_)):
            temp = arr_[idx_]

            while arr_[idx_ - 1] > temp:
                arr_[idx_] = arr_[idx_ - 1]
                idx_ -= 1
            arr_[idx_] = temp

    buckets = tuple([] for _ in range(k))
    m = max(arr)

    for val in arr:
        buckets[(k * val) // (m + 1)].append(val)

    for i in range(1, k):
        insertion(buckets[i])

    for idx, val in enumerate(chain(*buckets)):
        arr[idx] = val


def grail_INCOMPLETE(arr):
    def swap(arr_, idx1, idx2):
        arr_[idx1], arr_[idx2] = arr_[idx2], arr_[idx1]

    def block_swap(arr_, start1, start2, block_size):
        for idx in range(block_size):
            swap(arr_, start1 + idx, start2 + idx)

    def rotate(arr_, start, length, amount):
        while length and amount:
            if length <= amount:
                block_swap(arr_, start, start + length, amount)
                start += length
                amount -= length
            else:
                block_swap(arr_, start + length - amount, start + length, amount)
                length -= amount


def WikiSort_INCOMPLETE(arr: MutableSequence, _64bit=False):
    import itertools
    """Implementation based on:
    https://github.com/BonzaiThePenguin/WikiSort/blob/master/Chapter%201.%20Tools.md"""

    def swap(arr_, idx1, idx2):
        arr_[idx1], arr_[idx2] = arr_[idx2], arr_[idx1]

    def linear(arr_, range_: range, val):
        for idx in range_:
            if arr_[idx] == val:
                return idx

    def reverse(arr_, range_: range):
        for idx in range(len(range_) // 2 - 1, -1, -1):
            swap(arr_, range_.start + idx, range_.stop - idx - 1)

    def block_swap(arr_, start1, start2, block_size):
        for idx in range(block_size):
            swap(arr_, start1 + idx, start2 + idx)

    def pull(range_):
        pass

    def rotate(arr_, range_: range, amount):
        if len(range_) == 0:
            return

        split = range_.start + amount if amount >= 0 else range_.stop + amount

        reverse(arr_, range(range_.start, split))
        reverse(arr_, range(split, range_.stop))
        reverse(arr_, range_)

    def _binary_main(arr_, range_: range, val, comp):
        start = range_.start
        end = range_.stop
        while start < end:
            mid = start + (end - start) // 2
            if comp(arr_[mid], val):
                start = mid + 1
            else:
                end = mid

        if start == range_.stop - 1 and comp(arr_[start], val):
            start += 1
        return start

    def binary_first(arr_, val, range_: range):
        return _binary_main(arr_, range_, val, lambda x, y: x < y)

    def binary_last(arr_, val, range_: range):
        return _binary_main(arr_, range_, val, lambda x, y: x <= y)

    def _find_forward_main(arr_, val, range_, unique, comp):
        if len(range_) == 0:
            return range_.start

        skip = max(len(range_) // unique, 1)

        for idx in itertools.count(range_.start + skip, skip):
            if not comp(arr_[idx - 1], val):
                break
            if idx >= range_.stop - skip:
                return binary_first(arr_, val, range(idx, range_.stop))

        return binary_first(arr_, val, range(idx - skip, idx))

    def find_first_forward(arr_, val, range_: range, unique: int):
        return _find_forward_main(arr_, val, range_, unique, lambda x, y: x < y)

    def find_last_forward(arr_, val, range_: range, unique: int):
        return _find_forward_main(arr_, val, range_, unique, lambda x, y: x <= y)

    def _find_backward_main(arr_, val, range_: range, unique: int, comp):
        if len(range_) == 0:
            return range_.start

        skip = max(len(range_) // unique, 1)

        for idx in itertools.count(range_.stop - skip, skip):
            if not (idx > range_.start and comp(val, arr_[idx - 1])):
                break

            if idx < range_.start + skip:
                return binary_first(arr_, val, range(range_.start, idx))
            return binary_first(arr_, val, range(idx, idx + skip))

    def find_first_backward(arr_, val, range_, unique):
        return _find_backward_main(arr_, val, range_, unique, lambda x, y: x <= y)

    def find_last_backward(arr_, val, range_, unique):
        return _find_backward_main(arr_, val, range_, unique, lambda x, y: x < y)

    def length_gen(start_, stop_, multiply_factor=1):
        """Step is self value."""
        curr = start_
        while curr < stop_:
            yield curr
            curr *= multiply_factor

    def insertion(arr_: MutableSequence, start_, end_):
        for i in range(start_ + 1, end_):
            j, temp = i, arr_[i]

            while j > start_ and arr_[j - 1] > temp:
                arr_[j] = arr_[j - 1]
                j -= 1
            arr_[j] = temp

    def merge_in_place(arr_, range_a, range_b):
        if len(range_a) == 0 or len(range_b) == 0:
            return

        range_a_ = range_a
        range_b_ = range_b

        while True:
            mid_ = binary_first(arr_, arr_[range_a_.start], range_b_)

            amount = mid_ - range_a_.stop
            rotate(arr_, range(range_a_.start, mid_), -amount)
            if range_b_.stop == mid_:
                break

            range_b_ = range(mid_, range_b_.stop)
            range_a_ = range(range_a_.start + amount, range_b_.start)
            range_a_ = range(binary_last(arr_, arr_[range_a_.start], range_a_), range_a_.stop)
            if len(range_a_) == 0:
                break

    def net_swap(arr_, order, range_: range, x, y):
        result = arr_[range_.start + x] > arr_[range_.start + y]
        if result or (order[x] > order[y] and arr_[range_.start + x] == arr_[range_.start + y]):
            swap(arr_, range_.start + x, range_.start + y)
            swap(order, x, y)

    def iterator_(size, min_level):
        def floor_by_power_2(x: int):
            for n in range(6 if _64bit else 5):
                x = x | (x >> 2 ** n)
            else:
                return x - (x >> 1)

        power_of_two = floor_by_power_2(size)
        denominator = power_of_two // min_level
        numerator_step = size % denominator
        decimal_step = size // denominator

        numerator, decimal = 0, 0

        def generator():
            nonlocal numerator, decimal
            while decimal_step < size:
                start = decimal
                decimal += decimal_step
                numerator += numerator_step
                if numerator >= denominator:
                    numerator -= denominator
                    decimal += 1

                yield range(start, decimal)

        def next_level():
            nonlocal decimal_step, numerator_step
            decimal_step *= 2
            numerator_step *= 2
            if numerator_step >= denominator:
                numerator_step -= denominator
                decimal_step += 1

            return decimal_step < size

        generator.next_level = next_level
        return generator()

    def sort(arr_):
        size = len(arr_)
        if size < 4:
            if size == 3:
                if arr_[1] < arr_[0]:
                    swap(arr_, 1, 0)

                if arr_[2] < arr_[1]:
                    swap(arr_, 2, 1)

                    if arr_[1] < arr_[0]:
                        swap(arr_, 1, 0)
            elif size == 2:
                if arr_[1] < arr_[0]:
                    swap(arr_, 1, 0)

        iterator = iterator_(size, 4)
        for range_ in iterator:
            order = array.array(range(8))

            if len(range_) == 8:
                for i in range(0, 8, 2):
                    net_swap(arr_, order, range_, i, i + 1)

                net_swap(arr_, order, range_, 0, 2)
                net_swap(arr_, order, range_, 1, 3)
                net_swap(arr_, order, range_, 4, 6)
                net_swap(arr_, order, range_, 5, 7)
                net_swap(arr_, order, range_, 1, 2)
                net_swap(arr_, order, range_, 5, 6)
                net_swap(arr_, order, range_, 0, 4)
                net_swap(arr_, order, range_, 3, 7)
                net_swap(arr_, order, range_, 1, 5)
                net_swap(arr_, order, range_, 2, 6)
                net_swap(arr_, order, range_, 1, 4)
                net_swap(arr_, order, range_, 3, 6)
                net_swap(arr_, order, range_, 2, 4)
                net_swap(arr_, order, range_, 3, 5)
                net_swap(arr_, order, range_, 3, 4)

            elif len(range_) == 7:
                net_swap(arr_, order, range_, 1, 2)
                net_swap(arr_, order, range_, 3, 4)
                net_swap(arr_, order, range_, 5, 6)
                net_swap(arr_, order, range_, 0, 2)
                net_swap(arr_, order, range_, 3, 5)
                net_swap(arr_, order, range_, 4, 6)
                net_swap(arr_, order, range_, 0, 1)
                net_swap(arr_, order, range_, 4, 5)
                net_swap(arr_, order, range_, 2, 6)
                net_swap(arr_, order, range_, 0, 4)
                net_swap(arr_, order, range_, 1, 5)
                net_swap(arr_, order, range_, 0, 3)
                net_swap(arr_, order, range_, 2, 5)
                net_swap(arr_, order, range_, 1, 3)
                net_swap(arr_, order, range_, 2, 4)
                net_swap(arr_, order, range_, 2, 3)

            elif len(range_) == 6:
                net_swap(arr_, order, range_, 1, 2)
                net_swap(arr_, order, range_, 4, 5)
                net_swap(arr_, order, range_, 0, 2)
                net_swap(arr_, order, range_, 3, 5)
                net_swap(arr_, order, range_, 0, 1)
                net_swap(arr_, order, range_, 3, 4)
                net_swap(arr_, order, range_, 2, 5)
                net_swap(arr_, order, range_, 0, 3)
                net_swap(arr_, order, range_, 1, 4)
                net_swap(arr_, order, range_, 2, 4)
                net_swap(arr_, order, range_, 1, 3)
                net_swap(arr_, order, range_, 2, 3)

            elif len(range_) == 5:
                net_swap(arr_, order, range_, 0, 1)
                net_swap(arr_, order, range_, 3, 4)
                net_swap(arr_, order, range_, 2, 4)
                net_swap(arr_, order, range_, 2, 3)
                net_swap(arr_, order, range_, 1, 4)
                net_swap(arr_, order, range_, 0, 3)
                net_swap(arr_, order, range_, 0, 2)
                net_swap(arr_, order, range_, 1, 3)
                net_swap(arr_, order, range_, 1, 2)

            elif len(range_) == 4:
                net_swap(arr_, order, range_, 0, 1)
                net_swap(arr_, order, range_, 2, 3)
                net_swap(arr_, order, range_, 0, 2)
                net_swap(arr_, order, range_, 1, 3)
                net_swap(arr_, order, range_, 1, 2)

            if size < 8:
                return


if __name__ == '__main__':
    from async_main import generate_test

    testcase = generate_test(20)
    # WikiSort_in_place(testcase)
    # Merge_inplace_rotation(testcase)
    print(testcase)
