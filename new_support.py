import array
from collections.abc import MutableSequence, Iterable
from new_color_support import red, green, blue, cyan, purple


class ArrayWrap(MutableSequence):
    color_map = {
        'default': lambda x: x,
        'get': blue,
        'del': red,
        'set': cyan,
        'sorted': green
    }

    def __init__(self, source: (MutableSequence, Iterable)):
        self.arr = array.array('i', source)
        self.color_mapping = [self.color_map['default'] for _ in range(len(self.arr))]

        self.access = 0
        self.write = 0

        self.aux_arr = array.array('i')
        self.aux_arr.extend(0 for _ in range(len(self.arr)))
        self.aux_access = 0
        self.aux_write = 0

    def __repr__(self):
        return str(self.arr)

    def insert(self, index: int, o) -> None:
        # print("Called insert")
        self.arr.insert(index, o)

    def __getitem__(self, i: (int, slice)):
        try:
            self.on_call(i, 'get')
        except TypeError:
            if isinstance(i, slice):
                for idx in range(i.start, i.stop, i.step if i.step else 1):
                    self.on_call(idx, 'get')

        return self.arr[i]

    def __setitem__(self, i: int, o) -> None:
        self.on_call(i, 'set')
        self.arr[i] = o

    def __delitem__(self, i: int) -> None:
        self.on_call(i, 'del')
        self.arr.pop(i)

    def __len__(self) -> int:
        return len(self.arr)

    def on_call(self, idx, action: str):
        color_func = self.color_map[action]
        self.color_mapping[idx] = color_func

    def apply_color_map(self):
        return [f(v) for f, v in zip(self.color_mapping, self.arr)]


if __name__ == '__main__':

    test = ArrayWrap(i for i in range(20))
    print(*test.apply_color_map())
    print(*test[2:5])
    print(*test.apply_color_map())
