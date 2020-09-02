import unittest

import Sorting_algorithms_pure as SAP


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
        global results
        results = []

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

    def test_Random_20(self):

        correct = generate(20)
        test = shuffle_generate(20)

        self.assertEqual(correct, Loader(test))
        Better_output(test, correct)

    def test_Random_10(self):

        correct = generate(10)
        test = shuffle_generate(10)

        self.assertEqual(correct, Loader(test))
        Better_output(test, correct)

    def test_Zero_10(self):

        correct = generate(10, 0)
        test = shuffle_generate(10, 0)

        self.assertEqual(correct, Loader(test))
        Better_output(test, correct)


if __name__ == '__main__':
    unittest.main()
    global results

