import unittest
import array
from MutableWrapper import PrintingCountingMutable
from async_main import generate_test, select_sorts_list


class ArraySortTest(unittest.TestCase):
    targets = []


def paired_test_gen(size):
    return [i + 1 for i in range(size)], generate_test(size)


def add_test_dynamic(sort_list: list):
    """Monkey-patches Test class to dynamically add tests."""

    def closure(size, sort_type):
        def test_template(self):

            source, test = paired_test_gen(size)
            sort_type(test)
            self.assertEqual(source, test)

        return test_template

    for size_ in (30, 200):
        for sort in sort_list:
            setattr(ArraySortTest, f"test_{sort.__name__}_random_{size_}", closure(size_, sort))


if __name__ == '__main__':
    targets = select_sorts_list()
    add_test_dynamic(targets)
    unittest.main()
