import time
import g_var

# Created by looking at pseudo code in en wiki

__all__ = ['Bubble', 'Bubble_opt1', 'Bubble_opt2', 'Selection']


# Cleanup Color marks and let Visual thread end of thread.

def end():
    g_var.Color_reset()
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
        
        #self.access = 0
        #self.swap = 0
    
    
    def lo_list(self, index):
        self.event.wait()
        self.event.clear()
        g_var.Color_reset()
        
        g_var.selected = index
        g_var.access += 1
        #self.access += 1
        
        return self.array[index]
    
    
    def lo_compare(self, idx1, idx2):
        self.event.wait()
        self.event.clear()
        g_var.Color_reset()
        
        # TODO: add mode trigger to enable compare colouring or not
        # return 1 if self.lo_list(self, idx1) > self.lo_list(self, idx2) else 0
        
        #g_var.selected = idx1
        g_var.access += 2
        g_var.comp_target = [idx1, idx2]
        
        return 1 if self.array[idx1] > self.array[idx2] else 0

    
    def lo_swap(self, idx1, idx2):
        self.event.wait()
        self.event.clear()
        g_var.Color_reset()
        
        g_var.access += 2
        g_var.swap += 1
        #self.access += 2
        #self.swap += 1
        
        #g_var.selected = [idx1, idx2]
        g_var.swap_target = [idx1, idx2]
        
        Swap(self.array, idx1, idx2)
        

class Bubble(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        swapped = True
        
        while swapped:
            swapped = False

            for idx in range(self.length-1):
                if self.lo_compare(idx, idx+1):

                    swapped = True
                    self.lo_swap(idx, idx+1)
        
        end()
        return None
    
    # this don't do anything unless used like 'with bubble as bla bla'
    '''
    def __exit__(self):
        end()
        print('Sorted')
    '''

        
class Bubble_opt1(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        swapped = True
        n = self.length

        while swapped:
            swapped = False
            
            for idx in range(n-1):
                if self.lo_compare(idx, idx+1):
                    swapped = True
                    self.lo_swap(idx, idx+1)
            n -= 1
        
        end()
        return None
    
    
class Bubble_opt2(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        n = self.length

        while True:
            newn = 0
            
            for idx in range(n-1):
                if self.lo_compare(idx, idx+1):
                    self.lo_swap(idx, idx+1)
                    newn = idx+1
                    
            n = newn
            
            if n <= 1:
                break
        
        end()
        return None
    
    
class Cocktail_shaker(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        # improve this function, not gonna watch pseudo code yet
        swapped = True
        flip = False
        l = self.length
        n = self.length
        n2 = self.length
        
        while swapped:
            swapped = False

            if flip:
                flip = False

                for idx in range(n2-1, l-n, -1):

                    if self.lo_compare(idx-1,idx):
                        swapped = True
                        self.lo_swap(idx-1, idx)
                n -= 1

            else:
                flip = True

                for idx in range(l-n, n2-1):

                    if self.lo_compare(idx,idx+1):
                        swapped = True
                        self.lo_swap(idx, idx+1)
                n2 -= 1

        end()
        return None


    