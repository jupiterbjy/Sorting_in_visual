import time
import g_var

# Created by looking at pseudo code in en wiki
#__all__ = []

# marks end of class
def end():
    g_var.s_alive = False
    

# Not sure if this was good idea
    
class Sort():
    def __init__(self, Class):
        self.array = Class.array
        self.length = len(Class.array)
        self.event = g_var.ev
        self.swapped = True
    
    # Don't forget to put 'self' on all function in class!
    
    def swap(self, a, b, c):
        a[b], a[c] = a[c], a[b]
    
    
# Is it better to set self.swapped to some label rather than just spamming .self?

class Bubble(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        while self.swapped:
            self.swapped = False

            for idx in range(self.length-1):
                self.event.wait()

                if self.array[idx] > self.array[idx+1]:

                    self.swapped = True
                    self.swap(self.array, idx, (idx+1))

                self.event.clear()
        
        return None

    def __exit__(self):
        end()
        print('Sorted')
    
    
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


    
