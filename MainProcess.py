import threading as th
import psutil
import os
import tqdm
from time import sleep

import Source_array
import Sorting_algorithms as Sort_al
import g_var

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
    # TODO: Find a way to print in smaller Area, like using half-sized charactors.
    # TODO: set Blue for Current, Red for Min. Item, Yellow for sorted. (for selection sort.)
    
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
                
            print(color + "█" * i + ANSI_C.END, sep='', end='\n')
        
        out = ["Frame : " + str(frame)]
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
            return Sort_al.__all__[sel]

        except Exception as ex:
            print(ex, "/ Try again.")
        
        
def Check_ANSI():
    if psutil.Process(os.getpid()).parent().name() != 'bash':
        
        print("Running on CMD, Importing Colorama.init")
        from colorama import init
        
        init()
        
    else:
        print("Running on ANSI compatable Terminal.")
    
    sleep(1)

def Get_testcase():
    print("[ Type 0 or string to use default value ]")
    # Bad usage of try-except? idk, no time to fix this now.
    
    try:
        item_count = int(input("Type Number of items to sort: "))
    except:
        item_count = 0
    
    try:
        delay = int(input("Type delay in milisecond(s): "))/1000
    except:
        delay = 0
    
    return (item_count if item_count > 0 else 20, delay if delay > 0 else 0.05)
    
    
if __name__ == '__main__':
    # running as main
    
    Check_ANSI()
    
    
    test_case = Source_array.Source(*Get_testcase())  #  * as unpacker!
    
    sorter = th.Thread(target = getattr(Sort_al, Al_loader()), args = (test_case,))
    visual = th.Thread(target = Visualizing, args = (test_case,))
    
    
    sorter.start()
    visual.start()
    
    
else:
    # imported 
    pass
