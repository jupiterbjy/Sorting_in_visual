# Global variable storage
from threading import Event

ev = Event()
flag = False
s_alive = True
selected = 0
swap_target = -1

access = 0
swap = 0