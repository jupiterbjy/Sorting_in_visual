from multiprocessing import Process, Lock
import threading as th
from time import sleep

import Source_array
import Sorting_algorithms as Algorithms
import g_var


# Don't put () on target, or it will return result of that function!

# Having headache searching how to run thread, darn.

class ANSI_C():
    HEADER = '\033[95m'
    RED = '\033[91m'
    GRN = '\033[92m'
    BLU = '\033[94m'
    YEL = '\033[93m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Visualizing(Class):
    # Vertical for now
    
    frame = 0
    while g_var.s_alive:
        sleep(Class.delay)
        
        print("\n\n", "_" * Class.length, sep='')
        
        for idx, i in enumerate(Class.array):
            
            if idx == g_var.swap_target:
                color = ANSI_C.GRN
                
            else:
                color = ANSI_C.YEL if idx == g_var.selected else ANSI_C.END
                
            print(color + "#" * i + ANSI_C.END, sep='', end='\n')
        
        #out = "Frame:" + str(frame).rjust(8) + "Access:".rjust(14) + str(g_var.access).rjust(22)
        out = "Frame : " + str(frame) + "\nAccess: " + str(g_var.access) + "\nSwap  : " + str(g_var.swap)
        
        print("_" * Class.length, sep='')
        print(out)

        frame += 1
        g_var.ev.set()
    
    print("Sort complete")
        

# Will load up entire list of sorts and run one by one, far way to go.     
class Loader():
    def __init__(self, al_list):
        pass
        # do something
        
    def __exit__(self):
        pass
        # kill process or reset 'source' instance, idk
        
    
if __name__ == '__main__':
    # running as main
    test_case = Source_array.Source(10, 0.1)
    
    changed = th.Event()
    
    sorter = th.Thread(target = Algorithms.Bubble_opt1, args = (test_case,))
    visual = th.Thread(target = Visualizing, args = (test_case,))
    
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
