from multiprocessing import Process, Lock
import threading as th
from time import sleep

import Source_array
import Sorting_algorithms as Algorithms
import g_var


# Don't put () on target, or it will return result of that function!

# Having headache searching how to run thread, darn.

class ANSI_C():
    
    RED = '\033[91m'
    GRN = '\033[92m'
    BLU = '\033[94m'
    YEL = '\033[93m'
    PUR = '\033[94m'
    CYA = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'
    HEADER = '\033[95m'
    UNDERLINE = '\033[4m'
    
    table = {
        "RED" : '\033[91m',
        "GRN" : '\033[92m',
        "BLU" : '\033[94m',
        "YEL" : '\033[93m',
        "PUR" : '\033[94m',
        "CYA" : '\033[96m',
        "END" : '\033[0m',
        "BOLD" : '\033[1m',
        "HEADER" : '\033[95m',
        "UNDERLINE" : '\033[4m',
    }
    
    
def Colorize(txt, color):
    s = str(txt)
    return ANSI_C.table[color] + s + ANSI_C.table["END"]
        

class Selection_page():
    pass
    
    
def Visualizing(Class):
    # Vertical for now
    # TODO: add more color detail and print sorting algorithms' name
    
    frame = 0
    while g_var.s_alive:
        sleep(Class.delay)
        
        print("\n\n", "_" * Class.length, sep='')
        
        for idx, i in enumerate(Class.array):
            if idx in g_var.comp_target:
                color = ANSI_C.YEL
            
            elif idx in g_var.swap_target:
                color = ANSI_C.PUR
                
            else:
                color = ANSI_C.END
                #color = ANSI_C.GRN if idx == g_var.index else ANSI_C.END
                
            print(color + "#" * i + ANSI_C.END, sep='', end='\n')
        
        #out = "Frame:" + str(frame).rjust(8) + "Access:".rjust(14) + str(g_var.access).rjust(22)
        out = ["Frame : " + str(frame)]
        out.append("Access: " + Colorize(g_var.access, 'YEL'))
        out.append("Swap  : " + Colorize(g_var.swap, 'PUR'))
        
        print("_" * Class.length, sep='')
        print('\n'.join(out))

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
    test_case = Source_array.Source(20, 0.07)
    
    '''
    lock = Lock()
    
    sorter = Process(target = Algorithms.Bubble, args = (test_case.array, lock))
    visual = Process(target = Visualizing, args = (test_case.array, test_case.delay))
    '''
    
    sorter = th.Thread(target = Algorithms.Cocktail_shaker, args = (test_case,))
    visual = th.Thread(target = Visualizing, args = (test_case,))
    
    
    sorter.start()
    visual.start()
    
    
else:
    # imported 
    pass
