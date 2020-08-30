import array
from collections.abc import MutableSequence, Iterable


class ArrayWrap(MutableSequence):

    def __init__(self, source: (MutableSequence, Iterable)):
        self.arr = array.array('i', source)
        self.access = 0
        self.write = 0

        self.aux_arr = array.array('i')
        self.aux_arr.extend(0 for _ in range(len(source)))
        self.aux_access = 0
        self.aux_write = 0

    def __repr__(self):
        return str(self.arr)

    def insert(self, index: int, o) -> None:
        # print("Called insert")
        self.arr.insert(index, o)

    def __getitem__(self, i: (int, slice)):
        # print("Called __getitem__")
        return self.arr[i]

    def __setitem__(self, i: int, o) -> None:
        # print("Called __setitem__")
        self.arr[i] = o

    def __delitem__(self, i: int) -> None:
        # print("Called __delitem__")
        self.arr.pop(i)

    def __len__(self) -> int:
        return len(self.arr)

