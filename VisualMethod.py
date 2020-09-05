from sys import stdout


def _clear():
    # might need module 'reprint'..
    stdout.write("\x1b[2J\x1b[H")


def inline(access, write, color_func_map, array, pad):
    print(
        *(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)), f"|{access} {write}"
    )


def inline_clear(access, write, color_func_map, array, pad):
    _clear()
    print(
        *(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)),
        f"\nGet: {access} | Set: {write}",
    )


def _horizontal():
    output = (" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇")

    def str_convert_gen(val: int, length):
        for _ in range(length // 7 + (1 if length % 7 != 0 else 0)):  # assuming arr max val is same as arr length.
            if val > 7:
                yield output[7]
                val -= 7
            else:
                yield output[val]
                val = 0

    def inner(access, write, color_func_map, array, pad):
        nonlocal str_convert_gen

        _clear()

        output_lines = []
        length = len(color_func_map)

        for val, func in zip(array, color_func_map):
            output_lines.append(tuple(map(func, str_convert_gen(val, length)))[::-1])

        print(*map(''.join, zip(*output_lines)), sep='\n')

        print(f"Get: {access} | Set: {write}")

    return inner


horizontal = _horizontal()
