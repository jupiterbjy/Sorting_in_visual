# Global variable storage
from threading import Event

ev = Event()
flag = False
s_alive = True
CMD = False

index = 0
access = 0
swap = 0

acce_target = []
swap_target = []
comp_target = []
sorted_area = []

markers = [swap_target, acce_target, comp_target, sorted_area]


def Color_reset(ALL=False):
    global index
    index = 0

    if ALL:
        for i in markers:
            i.clear()
    else:
        acce_target.clear()
        swap_target.clear()
        comp_target.clear()
