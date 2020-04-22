from sys import stdout
import collections

from ANSI_table import ANSI_C
from Tools import member_loader
import g_var


fast_p = stdout.write


def colorMatcher(index):
    # colors = [ANSI_C.YEL, ANSI_C.PUR, ANSI_C.RED, ANSI_C.END]

    # for target in g_var.markers, color in colors:
    # use zip next time

    if index in g_var.comp_target:
        color = ANSI_C.YEL

    elif index in g_var.acce_target:
        color = ANSI_C.BLU

    elif index in g_var.swap_target:
        color = ANSI_C.PUR

    elif index in g_var.sorted_area:
        color = ANSI_C.RED

    else:
        color = ANSI_C.END

    return color


# https://en.wikipedia.org/wiki/Block_Elements
# ▀ ▄ █
def vertical(array):
    n = len(array)

    def zipped(n1, n2):
        smaller = n1 if n1 < n2 else n2
        fast_p('█' * smaller)

        if n1 == n2:
            return

        out = '▄' if n1 < n2 else '▀'
        fast_p(out * abs(n2 - n1) + '\n')

    def single(num):
        fast_p('▀' * num + '\n')

    if n & 1:
        for i in range(n >> 1):
            zipped(array[i << 1], array[(i << 1) + 1])

        single(array[-1])

    else:
        for i in range(n >> 1):
            zipped(array[i << 1], array[(i << 1) + 1])


def zipped_Bar(array):
    output = (' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇')
    lines = []

    for step in range(1 + (len(array) >> 3)):
        out2 = []

        for idx, i in enumerate(array):
            out2.append(colorMatcher(idx))

            if (step + 1) * 8 > i >= step * 8:
                out2.append(output[i - step * 8])

            elif i < step * 8:
                out2.append(' ')

            else:
                out2.append('█')

            out2.append(ANSI_C.END)

        lines.append("".join(out2))

    for i in reversed(lines):
        fast_p(i + '\n')


def zipped_Num(array, digit=" "):
    lines = []
    for step in range(int(len(array) / 10)):
        out2 = []

        for idx, i in enumerate(array):
            out2.append(colorMatcher(idx))

            if (step + 1) * 10 > i >= step * 10:
                out2.append(("" + str(i - step * 10)))

            elif i < step * 10:
                out2.append(" ")

            else:
                out2.append(digit)

            out2.append(ANSI_C.END)

        lines.append("".join(out2))

    for i in lines[::-1]:
        fast_p(i)


__all__ = member_loader.ListFunction(__name__, blacklist=["colorMatcher", "Zipped_main"])
