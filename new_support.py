import array
import asyncio
from collections.abc import MutableSequence, Iterable
from new_color_support import red, green, blue, cyan, purple


class CountingMutable(MutableSequence):
    def __init__(self, source: (MutableSequence, Iterable) = None):
        try:
            self.arr = array.array('i', source)
        except TypeError:
            self.arr = array.array('i')

        self.access = 0
        self.write = 0

    def __repr__(self):
        return f"{str(self.arr)}, access = {self.access}, write = {self.write}"

    def insert(self, index: int, o) -> None:
        self.on_insert(index, o)
        self.arr.insert(index, o)

    def __getitem__(self, i: (int, slice)):
        try:
            self.on_get(i)
            self.access += 1

        except TypeError:
            if isinstance(i, slice):
                for idx in range(i.start, i.stop, i.step if i.step else 1):
                    self.on_get(idx)
                    self.access += 1

        return self.arr[i]

    def __setitem__(self, i: int, o) -> None:
        self.on_set(i)
        self.arr[i] = o
        self.write += 1

    def __delitem__(self, i: int) -> None:  # I don't think I'm gonna use it.
        self.on_del(i)
        del self.arr[i]

    def __len__(self) -> int:
        return len(self.arr)

    # Override below after inherit.
    # below functions will run before actual array manipulation -
    # You're guaranteed to have specific key / item until end of scope.

    def on_insert(self, idx, item):
        pass

    def on_get(self, idx):
        pass

    def on_set(self, idx):
        pass

    def on_del(self, idx):
        pass


class PrintingCountingMutable(CountingMutable):
    """
    Best tool to play with when learning MutableSequence!
    """
    def __init__(self):
        super().__init__()

    def on_insert(self, idx, item):
        print(f"insert item {item} at {idx}")

    def on_get(self, idx):
        print(f"get item {self.arr[idx]} at {idx}")

    def on_set(self, idx):
        print(f"set item {self.arr[idx]} at {idx}")

    def on_del(self, idx):
        print(f"del item {self.arr[idx]} at {idx}")


class ArrayWrap(CountingMutable):
    color_map = {
        'default': lambda x: x,
        'get': blue,
        'del': red,
        'set': cyan,
        'sorted': green
    }

    def __init__(self, source: (MutableSequence, Iterable), q: asyncio.Queue):

        super().__init__(source)
        self.color_mapping = [self.color_map['default'] for _ in range(len(self.arr))]
        self.queue = q

    def on_set(self, idx):
        self.on_call(idx, 'set')

    def on_get(self, idx):
        self.on_call(idx, 'get')

    def on_call(self, idx, action: str):
        self.apply_color_condition()

        color_func = self.color_map[action]
        self.color_mapping[idx] = color_func

        try:
            self.queue.put_nowait((self.access, self.write, tuple(self.color_mapping), tuple(self.arr)))
        except AttributeError:
            pass

    def apply_color_condition(self):
        for idx, n in enumerate(self.arr):
            if idx + 1 == n:
                self.color_mapping[idx] = self.color_map['sorted']
            else:
                self.color_mapping[idx] = self.color_map['default']
