import threading as th
from time import sleep, time
from sys import stdout

from ANSI_table import *
import Source_array
import Sorting_algorithms as Sort_al
import g_var
import Output_Type

fast_p = stdout.write


def Visualizing(Class, name, out_func):

    start_time = time()
    frame = 0

    while True:  # runs until sort process finishes

        fast_p("_" * Class.length + "\n")
        out_func(Class.array)
        out = [
            "Sort  : " + str(name),
            "Frame : " + str(frame),
            "Access: " + Colorize(g_var.access, "YEL"),
            "Swap  : " + Colorize(g_var.swap, "PUR"),
            "Time  : " + str(time() - start_time),
        ]

        fast_p("_" * Class.length + "\n")
        fast_p("\n".join(out))

        frame += 1

        sleep(Class.delay)
        g_var.ev.set()

        if g_var.s_alive:
            Clear_Screen()
        else:

            break

    print("Script Ended.")


def Lister(target, query, error="\n Try Again."):
    "list functions in module and let user select it."

    print("\n")

    # expecting list is no longer than hundred. per. module.
    for idx, func in enumerate(target.__all__):
        print(idx, " " * (3 - len(str(idx))), func, sep="")

    while True:
        try:
            sel = int(input(query))

            return target.__all__[sel]

        except Exception as ex:

            print(Colorize(ex, "RED"), error, end="\n\n")


def Output_Type_loader():
    return Lister(Output_Type, "\nType index of Output Method: ")


def Al_loader():
    return Lister(Sort_al, "\nType index of Function to Test: ")


def Sort_Wrapper(test_class, func):
    # Debugging function, using this for default now.
    try:
        sort = getattr(Sort_al, func)
        sort(test_class)

    except Exception as ex:

        g_var.s_alive = False
        sleep(2)
        print(ex)


def Get_testcase():
    # Bad usage of try-except? idk, no time to think of this now.
    # TODO: add output method description
    try:
        i_count = int(input("\nType Number of items to sort: "))

    except BaseException:
        i_count = 20

    try:
        delay = int(input("\nType delay in milisecond(s): ")) / 1000

    except BaseException:
        delay = 0

    return i_count, delay if delay > 0 else 0.05


if __name__ == "__main__":
    # TODO: add stack to store list of sorts to run in seq.

    print("[ Type nothing to use default value.    ]")
    print("[ Too low delay is not recommended.     ]", end="\n\n")

    Check_ANSI()
    sleep(0.2)

    test_func = Al_loader()
    test_out = Output_Type_loader()
    test_case = Source_array.Source(*Get_testcase())

    out_func = getattr(Output_Type, test_out)
    print(out_func)

    sorter = th.Thread(target=Sort_Wrapper, args=(test_case, test_func))
    visual = th.Thread(target=Visualizing, args=(test_case, test_func, out_func))

    sorter.start()
    visual.start()


else:

    Check_ANSI()
