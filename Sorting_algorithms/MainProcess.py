from multiprocessing import Process, Lock
from time import sleep

import Source_array
import Sorting_algorithms as Algorithms


# Don't put () on target, or it will return result of that function!

# Having headache searching how to run thread, darn.


def Visualizing(source, lock, sort_proc):
    
    while sort_proc.is_alive():
        lock.aquire()

        # Vertical for now
        
        for i in source.array:
            print("#" * i, sep='', end='\n')

        sleep(source.delay)
        lock.release()
        

# Will load up entire list of sorts and run one by one, far way to go.     
class Loader():
    def __init__(self, al_list):
        pass
        # do something
        
    def __exit__(self):
        pass
        # kill process or reset 'source' instance, idk
        
    
if __name__ == "__main__":
    # running as main
    
    lock = Lock()
    test_case = Source_array.Source(30)
    
    sorter = Process(target = Algorithms.Bubble, args = (test_case.array, lock))
    visual = Process(target = Visualizing, args = (test_case, lock, sorter))
    
    sorter.start()
    visual.start()
    
else:
    # imported 
    pass
