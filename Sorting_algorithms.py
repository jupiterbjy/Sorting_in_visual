import time
import g_var
import member_loader

'''
Created by looking at pseudo code in eng. wiki
Stores modified sorting algorithms based on 'pure' ones.
'''


def End():
    'Cleanup Color marks and let Visual thread end of thread.'
    g_var.Color_reset()
    g_var.ev.wait()
    g_var.s_alive = False


def Add_Sorted_Area(a1, a2=-1, b1=-1, b2=-1):
    'Generate sorted area'

    def gen_arr(a, b):
        return list(range(a, b + 1))

    if a2 == -1:
        tmp = [a1]

    elif b1 == -1 and b2 == -1:
        tmp = gen_arr(a1, a2)

    else:
        tmp = gen_arr(a1, a2) + gen_arr(b1, b2)

    g_var.sorted_area += (set(tmp) - set(g_var.sorted_area))


def Swap(a, b, c):
    a[b], a[c] = a[c], a[b]


# Not sure if this was good idea

class Sort():
    def __init__(self, Class):
        self.array = Class.array
        self.length = len(Class.array)
        self.event = g_var.ev

    def lo_list(self, idx):
        # self.event.wait()
        # self.event.clear()
        # g_var.Color_reset()

        g_var.access += 1
        return self.array[idx]

    def lo_assign(self, idx, value):
        g_var.access += 1
        self.array[idx] = value

    def lo_compare(self, idx1, idx2, equal=False):
        self.event.wait()
        self.event.clear()
        g_var.Color_reset()

        g_var.access += 2
        g_var.comp_target = [idx1, idx2]

        if equal:
            return 1 if self.array[idx1] >= self.array[idx2] else 0
        else:
            return 1 if self.array[idx1] > self.array[idx2] else 0

    def lo_swap(self, idx1, idx2):
        self.event.wait()
        self.event.clear()
        g_var.Color_reset()

        g_var.access += 2
        g_var.swap += 1
        g_var.swap_target = [idx1, idx2]

        Swap(self.array, idx1, idx2)


class Bubble(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        swapped = True

        while swapped:
            swapped = False

            for idx in range(self.length - 1):
                if self.lo_compare(idx, idx + 1):

                    swapped = True
                    self.lo_swap(idx, idx + 1)

        End()
        return None

    # this don't do anything unless used like 'with bubble as bla bla'
    '''
    def __exit__(self):
        End()
        print('Sorted')
    '''


class Bubble_opt1(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        swapped = True
        n = self.length

        while swapped:
            swapped = False

            for idx in range(n - 1):
                if self.lo_compare(idx, idx + 1):
                    swapped = True
                    self.lo_swap(idx, idx + 1)
            n -= 1

        End()
        return None


class Bubble_opt2(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        n = self.length

        while True:
            newn = 0

            for idx in range(n - 1):
                if self.lo_compare(idx, idx + 1):
                    self.lo_swap(idx, idx + 1)
                    newn = idx + 1

            n = newn

            if n <= 1:
                break

        End()
        return None


class Cocktail_shaker(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        swapped = True
        flip = False
        start = 0
        end = self.length - 1

        while swapped:
            swapped = False

            if flip:
                flip = False

                for idx in range(end, start, -1):

                    if self.lo_compare(idx - 1, idx):
                        swapped = True
                        self.lo_swap(idx - 1, idx)
                start += 1

                Add_Sorted_Area(0, start - 1)
            else:
                flip = True

                for idx in range(start, end):

                    if self.lo_compare(idx, idx + 1):
                        swapped = True
                        self.lo_swap(idx, idx + 1)
                end -= 1

                Add_Sorted_Area(end + 1, self.length)

        Add_Sorted_Area(0, self.length)
        End()
        return None


class Cocktail_shaker_opt1(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        start = 0
        end = self.length - 1
        import time

        while start <= end:
            new_end = start
            new_start = end

            for idx in range(start, end):
                if self.lo_compare(idx, idx + 1):
                    self.lo_swap(idx, idx + 1)
                    new_end = idx

            end = new_end

            Add_Sorted_Area(end + 1, self.length)

            for idx in range(end, start, -1):
                if self.lo_compare(idx - 1, idx):
                    self.lo_swap(idx - 1, idx)
                    new_start = idx - 1

            start = new_start

            Add_Sorted_Area(0, start)
        End()


class OddEven(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        swapped = True

        while swapped:
            swapped = False

            for idx in range(0, self.length - 1, 2):

                if self.lo_compare(idx, idx + 1):
                    swapped = True
                    self.lo_swap(idx, idx + 1)

            for idx in range(1, self.length - 1, 2):

                if self.lo_compare(idx, idx + 1):
                    swapped = True
                    self.lo_swap(idx, idx + 1)

        End()


class Selection(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        length = self.length

        for loop in range(length):
            largest = 0

            for idx in range(length - loop):
                if self.lo_compare(idx, largest):
                    largest = idx

            self.lo_swap(idx, largest)
            Add_Sorted_Area(idx, idx)

        End()


class Insertion(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        for i in range(1, self.length):
            j = i

            while j > 0 and self.lo_compare(j - 1, j):
                self.lo_swap(j, j - 1)
                j -= 1

                Add_Sorted_Area(0, i)

        End()


class Heap(Sort):
    # Boi, he's fast - reference from Kirb 8.0
    def __init__(self, Class):
        super().__init__(Class)

        def heapify(idx, heap_size):

            largest = idx
            l_idx = 2 * idx + 1
            r_idx = 2 * idx + 2

            if l_idx < heap_size and self.lo_compare(l_idx, largest):
                largest = l_idx

            if r_idx < heap_size and self.lo_compare(r_idx, largest):
                largest = r_idx

            if largest != idx:
                self.lo_swap(largest, idx)
                heapify(largest, heap_size)

        for i in range(self.length // 2 - 1, -1, -1):
            heapify(i, self.length)

        for i in range(self.length - 1, 0, -1):

            self.lo_swap(0, i)

            Add_Sorted_Area(i, i)

            heapify(0, i)

        Add_Sorted_Area(0, 0)
        End()


class Merge(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        L, R = 0, self.length - 1

        def List_Merge(left, right, mid):
            Sorted = []
            l, r, m = left, right, mid + 1

            while(l <= mid and m <= right):

                if self.lo_compare(m, l, equal=True):
                    Sorted.append(self.array[l])
                    l += 1
                else:
                    Sorted.append(self.array[m])
                    m += 1

            if l > mid:
                for idx in range(m, right + 1):
                    Sorted.append(self.array[idx])
            else:
                for idx in range(l, mid + 1):
                    Sorted.append(self.array[idx])

            for idx in range(right, left - 1, -1):
                #Status(vars(), ['time'])
                self.lo_assign(idx, Sorted.pop())
                Add_Sorted_Area(idx)

        def Sub_merge(left, right):

            if left < right:
                mid = (left + right) // 2
                Sub_merge(left, mid)
                Sub_merge(mid + 1, right)
                List_Merge(left, right, mid)

        Sub_merge(L, R)
        End()


class Quick(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        def Sub_Quick(left, right):

            if left < right:

                pivot_new = Partition(left, right)

                Sub_Quick(left, pivot_new)
                Add_Sorted_Area(left, pivot_new)

                Sub_Quick(pivot_new + 1, right)
                Add_Sorted_Area(pivot_new + 1, right)

        def Partition(left, right):

            mid = (right + left) // 2

            if self.lo_compare(left, mid):
                self.lo_swap(mid, left)

            if self.lo_compare(left, right):
                self.lo_swap(right, left)

            pivot = self.array[mid]

            while True:
                while self.lo_list(left) < pivot:
                    left += 1

                while self.lo_list(right) > pivot:
                    right -= 1

                if left >= right:
                    return right
                self.lo_swap(right, left)

        Sub_Quick(0, self.length - 1)

        End()


class Counting(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        # TODO: find a way to visualize this kid.

        m = max(self.array)
        tmp = self.array[::]

        counts = [0 for i in range(m + 1)]
        results = [0 for i in range(self.length)]

        for i in tmp:
            counts[i] += 1

        for i in range(m):
            counts[i + 1] += counts[i]

        for i in tmp:
            self.array[counts[i] - 1] = i
            counts[i] -= 1

        # for idx, i in enumerate(self.array):
        #    self.lo_assign(idx, i)

        End()


class Radix_LSD_Base2(Sort):
    def __init__(self, Class):
        super().__init__(Class)

        # def lo_generate_seq(self, reverse=False):

        def count_bits(n):
            if(n == 0):
                return 0
            else:
                return 1 + count_bits(n >> 1)

        def counting_sort_bitwise(pos):

            counts = [0, 0]
            results = [0 for i in range(self.length)]

            for i in self.array:
                counts[i >> pos & 1] += 1

            counts[1] += counts[0]

            # Don't [::-1] waste Memory of another array size?
            for i in self.array[::-1]:

                results[counts[i >> pos & 1] - 1] = i
                counts[i >> pos & 1] -= 1

            return results

        # TODO: visualize this baby with getting max, or somethin' idk

        digit = count_bits(max(self.array))

        for i in range(digit):
            
            self.array = counting_sort_bitwise(i)

        End()


__all__ = member_loader.ListClass(__name__, name_only=True, blacklist=['Sort'])
