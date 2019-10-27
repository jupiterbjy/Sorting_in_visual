# Global variable storage
from threading import Event

ev = Event()
flag = False
s_alive = True

index = 0
swap_target = []
comp_target = []

access = 0
swap = 0

def Color_reset():
    index = 0
    swap_target.clear()
    comp_target.clear()
