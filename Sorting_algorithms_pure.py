# Stores Function-formed algorithms for ease of self-creation
# TODO: find better word than 'creation', have no Dictionary for now.

def Swap(a, b, c):
    a[b], a[c] = a[c], a[b]

def Bubble(array):
    swaped = True
    n = len(array)
    
    while swaped:
        swaped = False
        
        for idx in range(n-1):
            
            if array[idx] > array[idx+1]:
                swaped = True
                Swap(array, idx, idx+1)
    return array


def Bubble_opt1(array):
    swaped = True
    n = len(array)
    idx = 0
    
    while swaped:
        swaped = False
        
        for idx in range(n-1):
            if array[idx] > array[idx+1]:
                swaped = True
                Swap(array, idx, idx+1)
        n -= 1
            
    return array


def Bubble_opt2(array):
    n = len(array)
    
    while(n <= 1):
        newn = 0
        
        for idx in range(n-1):
            if array[idx] > array[idx+1]:
                swaped = True
                Swap(array, idx, idx+1)
                newn = idx
        
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


    
