import unittest
import Sorting_algorithms as SA

class loader(testcase):
    for i in SA.__all__:
        print("<", i, ">")
        eval('SA.i' + '(testcase)')

class TestBasicOutput(unittest.TestCase):
    
    def Reversed(self):
        test = [20 - i for i in range(20)]
        correct = [i+1 for i in range(20)]
        test = loader(test)
        
        print(test, '\n', correct)
        self.assertEqual(correct, test)