__all__ = ['Check_ANSI', 'ANSI_C', 'Colorize']

from time import sleep
from psutil import Process
import os


def Check_ANSI(output = True):
    if Process(os.getpid()).parent().name() != 'bash':
        if output:
            print("ANSI incompetible, Importing Colorama.init")
            
        from colorama import init
        init()
        
    else:
        if output:
            print("Running on ANSI compatable Terminal.")
    
    sleep(0.5)

    
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
        
