from __future__ import annotations

import array
import asyncio
import queue
import time
from collections.abc import MutableSequence, Iterable
from VisualMethod.ANSIWrap import *


class CountingMutable(MutableSequence):
    def __init__(self, source: MutableSequence | Iterable = None):
        try:
            self.arr = array.array('i', source)
        except TypeError:
            self.arr = array.array('i')

        self.access = 0
        self.write = 0

    def __str__(self):
        return f"{str(self.arr)}, access = {self.access}, write = {self.write}"

    def insert(self, index: int, o) -> None:
        self.arr.insert(index, o)  # fail-fast

        self.write += 1
        self.on_insert(index, o)

    def __getitem__(self, i: (int, slice)):
        val = self.arr[i]  # creating unnecessary name to fail-fast.

        if isinstance(i, slice):
            for idx in range(i.start, i.stop, i.step if i.step else 1):
                self.access += 1
                self.on_get(idx)
        else:
            self.access += 1
            self.on_get(i)

        return val

    def __setitem__(self, i: int, o) -> None:
        self.arr[i] = o

        self.write += 1
        self.on_set(i)

    def __delitem__(self, i: int) -> None:  # I don't think I'm gonna use it.
        del self.arr[i]
        self.on_del(i)

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


# TODO: replace pointless asyncio usage
class PrintingCountingMutable(CountingMutable):
    """
    Best tool to play with when learning MutableSequence!
    """
    def __init__(self, source, show_all=False):
        super().__init__(source)
        self.flag = show_all

    def on_insert(self, idx, item):
        if self.flag:
            self.on_change()
        else:
            print(f"insert item {item} at {idx}")

    def on_get(self, idx):
        if self.flag:
            self.on_change()
        else:
            print(f"get item {self.arr[idx]} at {idx}")

    def on_set(self, idx):
        if self.flag:
            self.on_change()
        else:
            print(f"set item {self.arr[idx]} at {idx}")

    def on_del(self, idx):
        if self.flag:
            self.on_change()
        else:
            print(f"del item {self.arr[idx]} at {idx}")

    def on_change(self):
        print(self.arr)

    def __eq__(self, other):
        return True if self.arr == other.arr else False


class ArrayWrap(CountingMutable):
    color_map = {
        'default': lambda x: x,
        'get': br_yellow,
        'del': br_magenta,
        'set': br_red,
        'insert': br_cyan,
        'sorted': br_blue
    }

    def __init__(self, source: MutableSequence | Iterable, q: queue.Queue = None):

        super().__init__(source)
        self.color_mapping = [self.color_map['default'] for _ in range(len(self.arr))]
        self.queue = q

        self.print_directly = bool(q)

    def on_insert(self, idx, item):
        self.on_call(idx, 'insert')

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

        # self.delay_func()

    def apply_color_condition(self):
        for idx, n in enumerate(self.arr):
            if idx + 1 == n:
                self.color_mapping[idx] = self.color_map['sorted']
            else:
                self.color_mapping[idx] = self.color_map['default']

    def mark_all_sorted(self):
        return self.access, self.write, [self.color_map['sorted'] for _ in range(len(self.arr))], self.arr


class PromptingListWrapper(CountingMutable):
    def __init__(self, source: MutableSequence | Iterable):
        super().__init__(source)


