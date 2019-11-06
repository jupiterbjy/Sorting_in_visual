import inspect
from sys import modules

import member_loader

'''Stores Function-formed algorithms for ease of self-creation'''
# TODO: find better word than 'creation', have no Dictionary for now.
# import Sorting_algorithms_pure as sa

def Status(data, blacklist = []):
    'Used for Outputting variables with exceptions'
    
    output = []
    blacklist.append('END_indicator')
    
    for i in data.keys():
        for i2 in blacklist:
            if i2 == 'END_indicator':
                break
                
            if i2 in i:
                continue
            else:
                output.extend([i, str(data[i])])
    
    blacklist = []  #prevent storing previous items.
    print(' | '.join(output))
    

def Swap(a, b, c):
    a[b], a[c] = a[c], a[b]

def Bubble(array):
    swapped = True
    n = len(array)
    
    while swapped:
        swapped = False
        
        for idx in range(n-1):
            
            if array[idx] > array[idx+1]:
                swapped = True
                Swap(array, idx, idx+1)
    return array


def Bubble_opt1(array):
    swapped = True
    n = len(array)
    
    while swapped:
        swapped = False
        
        for idx in range(n-1):
            if array[idx] > array[idx+1]:
                swapped = True
                Swap(array, idx, idx+1)
        n -= 1
            
    return array

# In case more than one element is in final position, this is faster.
def Bubble_opt2(array):
    n = len(array)
    while True:
        newn = 0
        
        for idx in range(n-1):
            if array[idx] > array[idx+1]:
                Swap(array, idx, idx+1)
                newn = idx+1
        
        n = newn
        
        if n<=1:
            break
    return array


def Cocktail_shaker(array):
    swapped = True
    flip = False
    start = 0
    end = len(array)-1
    
    while swapped:
        swapped = False
        
        if flip:
            flip = False
            for idx in range(end, start, -1):
                if array[idx-1] > array[idx]:
                    swapped = True
                    Swap(array, idx-1, idx)
            start += 1
        
        else:
            flip = True
            for idx in range(start, end):
                if array[idx] > array[idx+1]:
                    swapped = True
                    Swap(array, idx, idx+1)
            end -= 1
            
    return array
    
    
    # idk why I spent 2 hours fixthing this. not sure why it's fixed.
    # needs further testing
def Cocktail_shaker_opt1(array):
    start = 0
    end = len(array)-1
    import time
    
    while start <= end:
        #time.sleep(0.2)
        new_end = start
        new_start = end
        
        for idx in range(start, end):
            if array[idx] > array[idx+1]:
                Swap(array, idx, idx+1)
                new_end = idx
        
        end = new_end

        #Status(vars(), ['time'])
        
        for idx in range(end, start, -1):
            if array[idx-1] > array[idx]:
                Swap(array, idx-1, idx)
                new_start = idx-1
                
        start = new_start
        
        #Status(vars(), ['time'])
            
    return array


def Selection(array):
    length = len(array)
    
    for loop in range(length):
        largest = 0
        
        for idx in range(length - loop):
            if array[idx] > array[largest]:
                largest = idx
                
        Swap(array, idx, largest)
    
    return array


__all__ = member_loader.ListFunction(__name__, name_only = True)
__all__.remove('Swap')