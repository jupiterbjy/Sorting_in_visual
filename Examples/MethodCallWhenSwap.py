from collections.abc import MutableSequence


class Test(MutableSequence):
    def __init__(self, *args):
        self.arr = [*args]

    def __repr__(self):
        return str(self.arr)

    def insert(self, index: int, o) -> None:
        print("Called insert")
        self.arr.insert(index, o)

    def __getitem__(self, i: int):
        print("Called __getitem__")
        return self.arr[i]

    def __setitem__(self, i: int, o) -> None:
        print("Called __setitem__")
        self.arr[i] = o

    def __delitem__(self, i: int) -> None:
        print("Called __delitem__")
        self.arr.pop(i)

    def __len__(self) -> int:
        return len(self.arr)


if __name__ == '__main__':
    lst = Test(1, 10)
    print(f"Before: {lst}")

    lst[0], lst[1] = lst[1], lst[0]
    print(f"After: {lst}")
    list()
