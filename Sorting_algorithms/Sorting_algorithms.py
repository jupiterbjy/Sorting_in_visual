import time
import g_var

# Created by looking at pseudo code in en wiki
#__all__ = []


def end():
    g_var.s_alive = False
    
def Swap(a, b, c):
    a[b], a[c] = a[c], a[b]
        

# Not sure if this was good idea
# TODO: Improve colouring or event wait/clear timing

class Sort():
    def __init__(self, Class):
        self.array = Class.array
        self.length = len(Class.array)
        self.event = g_var.ev
        self.swapped = True
        
        #self.access = 0
        #self.swap = 0
    
    def lo_list(self, index):
        self.event.wait()
        
        g_var.selected = index
        g_var.swap_target = -1
        g_var.access += 1
        #self.access += 1
        
        self.event.clear()
        return self.array[index]
        
    def lo_swap(self, index1, index2):
        self.event.wait()
        g_var.access += 2
        g_var.swap += 1
        #self.access += 2
        #self.swap += 1
        
        g_var.selected = index2
        g_var.swap_target = index1
        
        Swap(self.array, index1, index2)
        
        self.event.clear()
        
    
# Is it better to set self.swapped to some label rather than just spamming .self?

class Bubble(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        while self.swapped:
            self.swapped = False

            for idx in range(self.length-1):
                if self.lo_list(idx) > self.lo_list(idx+1):

                    self.swapped = True
                    self.lo_swap(idx, idx+1)
        
        end()
        return None
    
    # this don't do anything unless used like 'with bubble as bla bla'
    def __exit__(self):
        end()
        print('Sorted')

        
class Bubble_opt1(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        n = self.length
        idx = 0

        while self.swapped:
            self.swapped = False

            while(idx < n):
                print(self.array, idx)
                if self.array[idx] > self.array[idx+1]:
                    self.swapped = True
                    self.swap(self.array, idx, idx+1)

                idx += 1
                n -= 1

        return None

    
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
'''

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


    
