# Stores Function-formed algorithms for ease of self-creation
# TODO: find better word than 'creation', have no Dictionary for now.
# import Sorting_algorithms_pure as sa

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
    
    
def Cocktail_shaker_opt1(array):
    flip = False
    start = 0
    end = len(array)-1
    import time
    
    while start < end:
        
        new_end = end
        new_start = start
        
        time.sleep(1)
        
        if flip:
            flip = False
            
            for idx in range(end, start, -1):
                if array[idx-1] > array[idx]:
                    Swap(array, idx-1, idx)
                    new_end = idx
        
        else:
            flip = True
                         
            for idx in range(start, end):
                if array[idx] > array[idx+1]:
                    Swap(array, idx, idx+1)
                    new_start = idx
        
        new_start -= 1
        print(array, start, end)
            
    return array

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

def Selection():
    pass


    
