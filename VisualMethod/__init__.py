from . import Methods


def inline(access, write, color_func_map, array, pad, sort_name):
    print(
        *(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)), f"|{access} {write}"
    )


def inline_clear(access, write, color_func_map, array, pad, sort_name):
    Methods.clear()
    print(
        *(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)),
        f"\n{sort_name} | Get: {access} | Set: {write}",
    )


def _horizontal():
    output = (" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█")

    def str_convert_gen(val: int, length):
        for _ in range(length // 8 + (1 if length % 8 != 0 else 0)):  # assuming arr max val is same as arr length.
            if val > 8:
                yield output[8]
                val -= 8
            else:
                yield output[val]
                val = 0

    def inner(access, write, color_func_map, array, pad, sort_name):
        nonlocal str_convert_gen

        output_lines = []
        length = len(color_func_map)

        for val, func in zip(array, color_func_map):
            output_lines.append(tuple(map(func, str_convert_gen(val, length)))[::-1])

        Methods.go_back(length + 1)
        print(*map(''.join, zip(*output_lines)), sep='\n')

        print(f"{sort_name} | Get: {access} | Set: {write}")

    return inner


horizontal = _horizontal()
