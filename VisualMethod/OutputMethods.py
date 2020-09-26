from collections.abc import Sequence

try:
    from ANSIWrap import go_back, clear, bold  # idk what's wrong with pycharm relative importing
except ImportError:
    from .ANSIWrap import go_back, clear, bold


def inline(access, write, color_func_map, array, pad, sort_name):
    print(
        *(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)), f"|{access} {write}"
    )


def inline_clear(access, write, color_func_map, array, pad, sort_name):
    go_back(2)
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

        go_back(length + 1)
        print(*reversed(tuple(map("".join, zip(*output_lines)))), sep="\n")

        print(f"{sort_name} | Get: {access} | Set: {write}")

    return inner


def create_horizontal(output_table: Sequence, over=' '):
    """converts output with numeral system based on len(output_table).

    for i.e. ('!', '@', '#') will be mapped to (0, 1, 2) respectively.

    Also assuming int sorted is inside range from 1 to len(output_table) - 2"""

    lim = len(output_table) - 1

    def str_convert_gen(val: int, item_counts):
        for _ in range(item_counts // lim + (1 if item_counts % lim != 0 else 0)):
            try:
                yield output_table[val]
            except IndexError:
                yield over
                val -= lim
            else:
                val = 0
    return _horizontal(str_convert_gen)


# change to use str.translate()
horizontal_bar = create_horizontal((" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"), over="█")
horizontal_num = create_horizontal((" ", *(str(i) for i in range(1, 10)), bold("X")))
horizontal_dot = create_horizontal((" ", *map(bold, ".·˙")))  # this runs too slow


if __name__ == "__main__":
    n = 30
    test_func = [lambda x: x for _ in range(n)]
    test_val = [i + 1 for i in range(n)]

    test_suite = 100, 200, test_func, test_val, len(str(n)), "test"

    inline(*test_suite)
    horizontal_bar(*test_suite)
    horizontal_num(*test_suite)
    horizontal_dot(*test_suite)
