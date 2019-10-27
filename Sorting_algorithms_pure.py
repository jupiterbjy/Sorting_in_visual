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
    # improve this function, not gonna watch pseudo code yet
    swapped = True
    flip = False
    l = len(array)
    n = l-1
    n2 = l
    #TODO: debug why this keeps searching beyond where it needed to be
    while swapped:
        swapped = False
        
        if flip:
            flip = False
            print(array, "A", n2-1, l-n-1, -1)
            for idx in range(n2-1, l-n-1, -1):
                print(idx-1, idx)
                if array[idx-1] > array[idx]:
                    swapped = True
                    Swap(array, idx-1, idx)
            n -= 1
            
        else:
            flip = True
            print(array, "A", l-n-1, n2-1)
            for idx in range(l-n-1, n2-1):
                print(idx, idx+1)
                if array[idx] > array[idx+1]:
                    swapped = True
                    Swap(array, idx, idx+1)
            n2 -= 1
            
    return array
    
    
def Cocktail_shaker_opt1(array):
    swapped = True
    flip = False
    n = len(array)-1
    n2 = len(array)
    last_n = 0
    last_n2 = 0
    
    while swapped:
        swapped = False
        
        if flip:
            flip = False
            
            last_n = 0
            
            for idx in range(n-1, 0, -1):
                if array[idx] > array[idx+1]:
                    swapped = True
                    Swap(array, idx, idx+1)
                    last_n = idx
            n -= 1
            
        else:   
            flip = True
                         
            for idx in range(n2-1):
                if array[idx] > array[idx+1]:
                    swapped = True
                    Swap(array, idx, idx+1)
            n2 -= 1
            
    return array


def Selection():
    pass


    
