from ANSI_table import ANSI_C
import member_loader
import g_var


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


def Vertcial(array):
    for idx, i in enumerate(array):
        print(Color_matcher(idx), end='', sep='')
        print("█" * i + ANSI_C.END, sep='')


def Zipped_main(array, digit=' '):
    lines = []
    for step in range(int(len(array) / 10)):
        out2 = []

        for idx, i in enumerate(array):
            out2.append(Color_matcher(idx))

            if i < (step + 1) * 10 and i >= step * 10:
                out2.append(('' + str(i - step * 10)))

            elif i < step * 10:
                out2.append(' ')

            else:
                out2.append(digit)

            out2.append(ANSI_C.END)

        lines.append(''.join(out2))

    for i in lines[::-1]:
        print(i)


def Zipped(array):
    Zipped_main(array)


def Zipped_Filled(array):
    Zipped_main(array, '^')


__all__ = member_loader.ListFunction(
    __name__, name_only=True, blacklist=['Color_matcher', 'Zipped_main'])
