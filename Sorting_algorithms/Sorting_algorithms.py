import time

# Created by looking at pseudo code in en wiki

#__all__ = []

def swap(a, b, c):
    a[b], a[c] = a[c], a[b]

    
def Bubble(array, lock):
    swaped = True
    n = len(array)
    
    while swaped:
        swaped = False
        
        for idx in range(n):
            
            lock.aquire()
            
            if array[idx] > array[idx+1]:
                swaped = True
                swap(array, idx, idx+1)
                
            lock.release()
    return array


# Todo - impliment lock and complete code below:

def Bubble_opt1(array, lock):
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
