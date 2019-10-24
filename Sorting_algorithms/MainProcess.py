from multiprocessing import Process, Lock
import threading as th
from time import sleep

import Source_array
import Sorting_algorithms as Algorithms
import g_var


# Don't put () on target, or it will return result of that function!

# Having headache searching how to run thread, darn.


def Visualizing(array, delay):
    sleep(5)
    frame = 0
    while g_var.s_alive:
        
        # Vertical for now
        
        sleep(delay)
        for i in array:
            print("#" * i, sep='', end='\n')
        print("_" * len(array), frame, sep='', end='\n\n')

        frame += 1
        g_var.ev.set()
        

# Will load up entire list of sorts and run one by one, far way to go.     
class Loader():
    def __init__(self, al_list):
        pass
        # do something
        
    def __exit__(self):
        pass
        # kill process or reset 'source' instance, idk
        
    
if __name__ == "__main__":
    # running as main
    test_case = Source_array.Source(10, 0.3)
    
    changed = th.Event()
    
    sorter = th.Thread(target = Algorithms.Bubble, args = (test_case,))
    visual = th.Thread(target = Visualizing, args = (test_case.array, test_case.delay))
    
    '''
    lock = Lock()
    
    sorter = Process(target = Algorithms.Bubble, args = (test_case.array, lock))
    visual = Process(target = Visualizing, args = (test_case.array, test_case.delay))
    '''
    
    sorter.start()
    visual.start()
    
    
else:
    # imported 
    pass
