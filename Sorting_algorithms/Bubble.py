import time

def Bubble(array, length, delay = 0, signal = False):
    swap = True
    
    while swap:
        swap = False
        
        for idx in range(length):
            signal = True
            time.sleep(delay)
            
            if array[idx] > array[idx+1]:
                swap = True
                array[idx], array[idx+1] = array[idx+1], array[idx]
    return array
    
#def Opt_Bubble():
    