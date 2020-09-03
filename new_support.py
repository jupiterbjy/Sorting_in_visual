import array
import asyncio
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

    def __init__(self, source: (MutableSequence, Iterable), q: asyncio.Queue):
        self.arr = array.array('i', source)
        self.color_mapping = [self.color_map['default'] for _ in range(len(self.arr))]

        self.access = 0
        self.write = 0

        self.queue = q

    def __repr__(self):
        return str(self.arr)

    def insert(self, index: int, o) -> None:
        self.arr.insert(index, o)

    def __getitem__(self, i: (int, slice)):
        try:
            self.on_call(i, 'get')
            self.access += 1

        except TypeError:
            if isinstance(i, slice):
                for idx in range(i.start, i.stop, i.step if i.step else 1):
                    self.on_call(idx, 'get')
                    self.access += 1

        return self.arr[i]

    def __setitem__(self, i: int, o) -> None:
        self.on_call(i, 'set')
        self.arr[i] = o
        self.write += 1

    def __delitem__(self, i: int) -> None:  # I don't think I'm gonna use it.
        self.on_call(i, 'del')
        self.arr.pop(i)

    def __len__(self) -> int:
        return len(self.arr)

    def on_call(self, idx, action: str):
        self.apply_color_condition()

        color_func = self.color_map[action]
        self.color_mapping[idx] = color_func

        self.queue.put_nowait((self.access, self.write, tuple(self.color_mapping), tuple(self.arr)))

    def apply_color_condition(self):
        for idx, n in enumerate(self.arr):
            if idx + 1 == n:
                self.color_mapping[idx] = self.color_map['sorted']
            else:
                self.color_mapping[idx] = self.color_map['default']

    def clear_counter(self):
        self.access = 0
        self.write = 0
