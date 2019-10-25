# Stores Function-formed algorithms for ease of self-creation
# TODO: find better word than 'creation', have no Dictionary for now.


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


    
