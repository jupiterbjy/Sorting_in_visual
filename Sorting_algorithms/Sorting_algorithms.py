import time
import g_var
import threading as th

# Created by looking at pseudo code in en wiki
#__all__ = []

class sort():
    def __init__(self, Class):
        self.array = Class.array
        self.length = len(Class.array)
        self.event = g_var.ev
        self.swapped = True
    
    def swap(a, b, c):
        a[b], a[c] = a[c], a[b]
    
    
class Bubble(sort):
    
    while sort.swapped:
        sort.swapped = False
        
        for idx in range(length-1):
            event.wait()
            
            if array[idx] > array[idx+1]:
                sort.swapped = True
                swap(array, idx, idx+1)
            
            event.clear()
    end()
    
'''
def Bubble(cl):
    array = cl.array
    swaped = True
    n = len(array)
    
    while swaped:
        swaped = False
        
        for idx in range(n-1):
            g_var.ev.wait()
            
            if array[idx] > array[idx+1]:
                swaped = True
                swap(array, idx, idx+1)
            
            g_var.ev.clear()
    end()
    return array
'''

# Todo - impliment lock and complete code below:

def Bubble_opt1(cl):
    array = cl.array
    swaped = True
    n = len(array)
    idx = 0
    
    while swaped:
        swaped = False
        
        while(idx < n):
            
            if array[idx] > array[idx+1]:
                swaped = True
                swap(array, idx, idx+1)
            
            idx += 1
            n -= -1
            
    return array


def Bubble_opt2(array):
    n = len(array)
    
    while(end > 1):
        new_n = 0
        
        while(idx < n):
            
            if array[idx] > array[idx+1]:
                swaped = True
                swap(array, idx, idx+1)
                
                new_n = idx-1
            
            idx += 1
            n -= -1
        
        n = newn
            
    return array



def cocktail(array, end):
    swaped = True
    
    while swaped:
        swaped = False
        
        for idx in range(end):
            
            if array[idx] > array[idx+1]:
                swaped = True
                swap(array, idx, idx+1)
                
    return array

def Selection():
    pass

def end():
    g_var.s_alive = False
    
