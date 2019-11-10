from Source_array import shuffle
from ANSI_table import *


def heap_tester(array):
    a = array[::]
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        heapify(a, i, n)
    
    return a

    
def heap_vis(array):
    col = ANSI_C()
    print(array)
    n = len(array)
    
    d = []
    
    def P(i, depth, out):
        
        left_idx = 2*i + 1
        right_idx = 2*i + 2
        
        if left_idx < n or right_idx < n:
            try:
                tmp = out[depth]
            
            except IndexError:
                out.append([[],[]])
            
            relay = []
            if left_idx < n:
                relay.append(str(array[left_idx]))
            
            if right_idx < n:
                relay.append(str(array[right_idx]))
                
            out[depth][0].append(f' {ANSI_C.BOLD}{array[i]}{ANSI_C.END}   ')
            out[depth][1].append('^'.join(relay) + ' ')
            
            if left_idx < n:
                P(left_idx, depth+1, out)
        
            if right_idx < n: 
                P(right_idx, depth+1, out)
            
        
    P(0, 0, d)
    max_width = 2**len(d)
    
    for idx, i in enumerate(d):
        print(''.join(i[0]) + '\n' + ''.join(i[1]))
    print('\n\n')
        
    
def heapify(unsorted, idx, heap_size):
    # Understand this more, next time!
        largest = idx
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        
        if left_idx < heap_size and unsorted[left_idx] > unsorted[largest]:
            largest = left_idx
            
        if right_idx < heap_size and unsorted[right_idx] > unsorted[largest]:
            largest = right_idx
            
        if largest != idx:
            unsorted[largest], unsorted[idx] = unsorted[idx], unsorted[largest]
            heapify(unsorted, largest, heap_size)

            
if __name__ == '__main__':
    source = [i+1 for i in range(20)]
    shuffle(source)
    heap_vis(source)
    
    
    heap_vis(heap_tester(source))
