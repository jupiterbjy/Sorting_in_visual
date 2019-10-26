# Global variable storage
from threading import Event

ev = Event()
flag = False
s_alive = True

selected = -1
swap_target = []
comp_target = []

access = 0
swap = 0

def Color_reset():
    selected = -1
    swap_target.clear()
    comp_target.clear()
