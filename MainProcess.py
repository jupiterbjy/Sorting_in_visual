import threading as th
import psutil
import os
import tqdm
from time import sleep

import Source_array
import Sorting_algorithms as Sort_al
import g_var
from ANSI_table import *

def Visualizing(Class, mode = 0):
    '''
    Visualizer for Sorting actions, currently only outputs in vertical way.
    '''
    # TODO: set Blue for Current, Red for Min. Item, Yellow for sorted. (for selection sort.)
    
    def Color_matcher(index):
        if index in g_var.comp_target:
            color = ANSI_C.YEL

        elif index in g_var.swap_target:
            color = ANSI_C.PUR

        elif index in g_var.sorted_area:
            color = ANSI_C.RED

        else:
            color = ANSI_C.END
            
        return color
                
    
    def Vertcial(array):
        for idx, i in enumerate(array):
            print(Color_matcher(idx), end='', sep='')
            print("█" * i + ANSI_C.END, sep='')
    
    
    def Zipped(array):
        lines = []
        for step in range(int(len(array)/10)):
            out2 = []
            
            for idx, i in enumerate(array):
                out2.append(Color_matcher(idx))
                
                if i < (step + 1) * 10 and i >= step * 10:
                    out2.append(('' + str(i - step * 10)))
                    
                elif i < step * 10:
                    out2.append(' ')
                    
                else:
                    out2.append('^')
                    
                out2.append(ANSI_C.END)
                    
            lines.append(''.join(out2))
            
        for i in lines[::-1]:
            print(i)
    
    
    frame = 0
    
    while g_var.s_alive:        #runs until sort process finishes
        sleep(Class.delay)

        print("\n\n", "_" * Class.length, sep='')

        if mode == 0:
            Vertcial(Class.array)
        else:
            Zipped(Class.array)
            
        global sort_name
        
        out = ["Sort  : " + str(sort_name)]
        out.append("Frame : " + str(frame))
        out.append("Access: " + Colorize(g_var.access, 'YEL'))
        out.append("Swap  : " + Colorize(g_var.swap, 'PUR'))

        print("_" * Class.length, sep='')
        print('\n'.join(out))

        frame += 1

        g_var.ev.set()
    
    print("Sort complete")
        
    
def Al_loader():
    for idx, func in enumerate(Sort_al.__all__):
        print(idx, func.rjust(5))
    
    while True:
        try:
            sel = int(input("Type index of Function to Test: "))
            global sort_name
            sort_name = Sort_al.__all__[sel]
            
            return Sort_al.__all__[sel]

        except Exception as ex:
            print(ex, "/ Try again.")

    
def Get_testcase():
    print("[ Type 0 or string to use default value ]")
    # Bad usage of try-except? idk, no time to fix this now.
    
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
    
    
    test_case = Source_array.Source(*Get_testcase())  #  * as unpacker!
    
    sorter = th.Thread(target = getattr(Sort_al, Al_loader()), args = (test_case,))
    visual = th.Thread(target = Visualizing, args = (test_case, mode))
    
    
    sorter.start()
    visual.start()
    
    
else:
    # imported 
    pass
