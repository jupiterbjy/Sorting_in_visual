import threading as th
from time import sleep, time

import Source_array
import Sorting_algorithms as Sort_al
import g_var
from Output_Type import *


def Visualizing(Class, mode = 0):
    
    '''
    Visualizer for Sorting actions, currently only outputs in vertical way.
    '''
    
    start_time = time()
    frame = 0
    
    while True:        #runs until sort process finishes
        
        print("_" * Class.length, sep='')

        if mode == 0:
            Vertcial(Class.array)
        else:
            Zipped(Class.array)
        
        global sort_name
        
        out = ["Sort  : " + str(sort_name)]
        out.append("Frame : " + str(frame))
        out.append("Access: " + Colorize(g_var.access, 'YEL'))
        out.append("Swap  : " + Colorize(g_var.swap, 'PUR'))
        out.append("Time  : " + str(time() - start_time))

        print("_" * Class.length, sep='')
        print('\n'.join(out))
        
        
        frame += 1

        sleep(Class.delay)
        g_var.ev.set()
            
        if g_var.s_alive:
            Clear_Screen()
        else:
            
            break
    
    print("Sort complete")
        
    
def Al_loader():
    for idx, func in enumerate(Sort_al.__all__):
        
        print(idx, ' ' * (3 - len(str(idx))), func, sep = '')
    
    while True:
        try:
            sel = int(input("Type index of Function to Test: "))
            global sort_name
            sort_name = Sort_al.__all__[sel]
            
            return Sort_al.__all__[sel]

        except Exception as ex:
            print(ex, "/ Try again.")

    
def Get_testcase():
    print('[ Type 0 or string to use default value ]')
    print('[ Too low delay is not recommended.     ]', end = '\n\n')
    # Bad usage of try-except? idk, no time to think of this now.
    
    try:
        i_count = int(input("Type Number of items to sort: "))
    except:
        i_count = 0
    
    try:
        delay = int(input("Type delay in milisecond(s): "))/1000
    except:
        delay = 0
        
    try:
        global mode
        mode = int(input("Type output method (0/1/2) : "))
    except:
        mode = 0
    
    return (i_count if i_count > 0 else 20, delay if delay > 0 else 0.05)
    
    
if __name__ == '__main__':
    global mode
    
    Check_ANSI()
    sleep(0.2)
    
    test_case = Source_array.Source(*Get_testcase())  #  * as unpacker!
    
    sorter = th.Thread(target = getattr(Sort_al, Al_loader()), args = (test_case,))
    visual = th.Thread(target = Visualizing, args = (test_case, mode))
    
    
    sorter.start()
    visual.start()
    
    
else:
    # imported 
    pass
