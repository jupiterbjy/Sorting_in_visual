from itertools import starmap

try:
    from . import Methods
except ImportError:
    import Methods  # idk what's wrong with pycharm relative importing

# TODO: use starmap


def inline(access, write, color_func_map, array, pad, sort_name):
    print(
        *(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)), f"|{access} {write}"
    )


def inline_clear(access, write, color_func_map, array, pad, sort_name):
    Methods.go_back(2)
    print(
        *(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)),
        f"\n{sort_name} | Get: {access} | Set: {write}",
    )


def _horizontal(convert_func):

    def inner(access, write, color_func_map, array, pad, sort_name):
        length = len(color_func_map)

        output_lines = [
            map(func, convert_func(val, length))
            for val, func in zip(array, color_func_map)
        ]

        Methods.go_back(length + 1)
        print(*reversed(tuple(map("".join, zip(*output_lines)))), sep="\n")

        print(f"{sort_name} | Get: {access} | Set: {write}")

    return inner


def _str_convert_wrapper(lim, output_table):

    def str_convert_gen(val: int, length):
        for _ in range(length // lim + (1 if length % lim != 0 else 0)):  # assuming arr max val is same as arr length.
            if val > lim:
                yield output_table[-1]
                val -= lim
            else:
                yield output_table[val]
                val = 0
    return str_convert_gen



def _num_conv_gen(val: int, length):
    for _ in range(length // 10 + (1 if length % 10 != 0 else 0)):
        if val > 10:
            yield ' '
            val -= 10

        elif val == 10:
            yield '0'
            val = 0

        else:
            yield str(val) if val else ' '
            val = 0


def _two_in_one_gen(val: int, length):
    for _ in range(length >> 1 + (1 if length & 1 != 0 else 0)):
        if val > 2:
            yield ' '
            val -= 2
        elif val == 2:
            yield '▀'
            val = 0
        else:
            if val:
                yield '▄'
                val = 0
            else:
                yield ' '


def _dot_triple_gen(val: int, length):
    pass


horizontal_bar = _horizontal(_str_convert_wrapper((" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█")))
horizontal_num = _horizontal(_num_conv_gen)
horizontal_block = _horizontal(_two_in_one_gen)

if __name__ == "__main__":
    n = 30
    test_func = [lambda x: x for _ in range(n)]
    test_val = [i for i in range(n)]

    horizontal_block(100, 200, test_func, test_val, len(str(n)), "test")
