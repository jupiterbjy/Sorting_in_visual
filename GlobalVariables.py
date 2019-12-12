# Global variable storage
from threading import Event

ev = Event()
flag = False
s_alive = True
CMD = False

# TODO: remove Source_array's testcase class
sort = None
delay = 0

index = 0
access = 0
swap = 0

acce_target = []
swap_target = []
comp_target = []
sorted_area = []

markers = [swap_target, acce_target, comp_target, sorted_area]