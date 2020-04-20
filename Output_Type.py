from ANSI_table import ANSI_C
from sys import stdout
import member_loader
import g_var
fast_p = stdout.write


def Color_matcher(index):
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
def Vertcial(array):
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


def Zipped_main(array, digit=" "):
    lines = []
    for step in range(int(len(array) / 10)):
        out2 = []

        for idx, i in enumerate(array):
            out2.append(Color_matcher(idx))

            if (step + 1) * 10 > i >= step * 10:
                out2.append(("" + str(i - step * 10)))

            elif i < step * 10:
                out2.append(" ")

            else:
                out2.append(digit)

            out2.append(ANSI_C.END)

        lines.append("".join(out2))

    for i in lines[::-1]:
        print(i)


def Zipped(array):
    Zipped_main(array)


def Zipped_Filled(array):
    Zipped_main(array, "^")


__all__ = member_loader.ListFunction(
    __name__, name_only=True, blacklist=["Color_matcher", "Zipped_main"]
)
