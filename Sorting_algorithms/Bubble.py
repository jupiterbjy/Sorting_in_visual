import Source_array as arr

def Bubble():
    
    swap = True
    arr.compare = 0
    arr.access = 0
    length = len(arr.array) - 1
    
    while swap:
        swap = False
        
        for idx in range(length):
            next = arr.array[idx+1]
            arr.compare += 1
            arr.access += 2
            
            # Not sure if should I count arr.access up by 1 if passing
            # second item to next first item, idk. Doing by 2 for now.
            
            if arr.array[idx] > next:
                swap = True
                
                arr.array[idx+1] = item
                arr.array[idx] = next
                
                arr.access += 2

def Opt_Bubble():
    