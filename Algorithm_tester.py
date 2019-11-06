import unittest
from threading import Thread, Event
import Sorting_algorithms_pure as SAP    

def Loader(testcase):
    for idx, item in enumerate(SAP.__all__):
        print(idx, item)
    
    out = getattr(SAP, SAP.__all__[int(input('Enter function to test:'))])
    
    return out(testcase)


class TestBasicOutput(unittest.TestCase):
    def setUp(self):
        global test, correct
        
        test = [20 - i for i in range(20)]
        correct = [i+1 for i in range(20)]
    
    
    def tearDown(self):
        print(test, '\n', correct)
    
    
    def test_Reversed(self):
        global test

        self.assertEqual(correct, Loader(test))

        
if __name__ == '__main__':
    unittest.main()