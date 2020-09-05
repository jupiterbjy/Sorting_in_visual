from sys import stderr


def _clear():
    stderr.write("\x1b[2J\x1b[H")


def inline(access, write, color_func_map, array, pad):
    print(*(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)), f"|{access} {write}")


def inline_clear(access, write, color_func_map, array, pad):
    _clear()
    print(*(f(f"{i:{pad}}") for f, i in zip(color_func_map, array)), f"\nGet: {access} | Set: {write}")
