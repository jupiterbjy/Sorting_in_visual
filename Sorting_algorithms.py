import time
import g_var

# Created by looking at pseudo code in en wiki
#__all__ = []


def end():
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
        self.swapped = True
        
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
        # will need event.wait() here then.
        
        # return 1 if self.lo_list(self, idx1) > self.lo_list(self, idx2) else 0
        g_var.access += 2
        #g_var.selected = idx1
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
        
        
# Is it better to set self.swapped to some label rather than just spamming .self?

class Bubble(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        while self.swapped:
            self.swapped = False

            for idx in range(self.length-1):
                if self.lo_compare(idx, idx+1):

                    self.swapped = True
                    self.lo_swap(idx, idx+1)
        
        end()
        return None
    
    # this don't do anything unless used like 'with bubble as bla bla'
    # Will leave this until I eventually use __exit__ method in this project, as a reminder.
    def __exit__(self):
        end()
        print('Sorted')

        
class Bubble_opt1(Sort):
    def __init__(self, Class):
        super().__init__(Class)
        
        n = self.length - 1
        idx = 0

        while self.swapped:
            self.swapped = False

            while(idx < n):
                if self.lo_list(idx) > self.lo_list(idx+1):
                    self.swapped = True
                    self.lo_swap(idx, idx+1)

                idx += 1
        n -= 1

        return None

    

