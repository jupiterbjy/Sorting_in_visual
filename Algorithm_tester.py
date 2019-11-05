import unittest
from threading import Thread, Event
import Sorting_algorithms_pure as SAP


def Loader(testcase):
    
    out = SAP.Cocktail_shaker(testcase)
    
    return out


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