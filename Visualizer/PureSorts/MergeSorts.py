from typing import MutableSequence
import array


# TODO: check stability on this: failed stability test. on Baekjoon.
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

def Merge_inplace_rotation(arr):
    import operator

    # https://www.geeksforgeeks.org/iterative-merge-sort/
    # https://xinok.wordpress.com/2014/08/17/in-place-merge-sort-demystified-2/

    def swap(arr_, a, b):
        arr_[a], arr_[b] = arr_[b], arr_[a]

    def reverse(arr_, range_: range):
        for idx in range(len(range_) // 2 - 1, -1, -1):
            swap(arr_, range_.start + idx, range_.stop - idx - 1)

    def rotate(arr_, range_: range, amount):
        if len(range_) == 0 or amount == 0:
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
        return _binary_main(arr_, range_, val, operator.lt)

    def binary_last(arr_, val, range_: range):
        return _binary_main(arr_, range_, val, operator.le)

    def merge(arr_, range_a, range_b):
        if len(range_a) == 0 or len(range_b) == 0:
            return

        range_a = range(range_a.start, range_a.stop)
        range_b = range(range_b.start, range_b.stop)

        while True:
            mid = binary_first(arr_, arr_[range_a.start], range_b)
            amount = mid - range_a.stop
            rotate(arr_, range(range_a.start, mid), -amount)
            if range_b.stop == mid:
                break

            range_b = range(mid, range_b.stop)
            range_a = range(range_a.start + amount, mid)
            range_a = range(binary_last(arr_, arr_[range_a.start], range_a), range_a.stop)
            if len(range_a) == 0:
                break

    def sub_merge(array_, left, right):

        if left < right:
            mid = (left + right) // 2
            sub_merge(array_, left, mid)
            sub_merge(array_, mid + 1, right)
            merge(array_, range(left, mid), range(mid, right))

    sub_merge(arr, 0, len(arr) - 1)
