import unittest
from threading import Thread, Event

import Sorting_algorithms_pure as SAP
from Source_array import shuffle


def Loader(testcase, secondrun=[]):
    # using kwarg's charactoristic to store run info
    if not secondrun:
        for idx, item in enumerate(SAP.__all__):
            print(idx, item)

        out = getattr(SAP, SAP.__all__[int(input('Enter function to test:'))])
        secondrun.append(out)
    else:
        out = secondrun[0]

    return out(testcase)


def Better_output(run, ans):
    try:
        global results
        tmp = '\ntest' + str(run) + '\n' + '\nansw' + str(ans)
        results.append(tmp)
    except NameError:
        results = []
        Better_output(run, ans)


class TestBasicOutput(unittest.TestCase):
    def setUp(self):
        global test, correct, test_10, correct_10

        test = [20 - i for i in range(20)]
        test_10 = [10 - i for i in range(10)]
        correct = test[::-1]
        correct_10 = test_10[::-1]

    def tearDown(self):
        global results
        for i in results:
            print(i)

    '''
    def test_Reversed(self):
        global test, correct

        Better_output(test, correct)
        self.assertEqual(correct, Loader(test))
    '''
    # a
    # Goorm, FIX DARN LINT FUNCTION ALREADY!!!!!!!!!!!!!!

    def test_Random_20(self):
        global test, correct

        test = shuffle(test)

        Better_output(test, correct)
        self.assertEqual(correct, Loader(test))

    def test_Random_10(self):
        global test_10, correct_10

        test_10 = shuffle(test_10)

        Better_output(test_10, correct_10)
        self.assertEqual(correct_10, Loader(test_10))


if __name__ == '__main__':
    unittest.main()
    global results

    