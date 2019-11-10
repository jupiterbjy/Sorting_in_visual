# Global variable storage
from threading import Event

ev = Event()
flag = False
s_alive = True
CMD = False

index = 0
access = 0
swap = 0

swap_target = []
comp_target = []
sorted_area = []

markers = [swap_target, comp_target, sorted_area]

def Color_reset(ALL = False):
    index = 0
    
    if ALL:
        for i in markers:
            i.clear()
    else:
        swap_target.clear()
        comp_target.clear()